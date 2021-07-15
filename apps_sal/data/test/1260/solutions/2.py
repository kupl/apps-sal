from enum import Enum

class OperationType(Enum):
	Multiply = 1
	Remove = 2

class RemoveOperation:
	def __init__(self, index):
		self.type = OperationType.Remove
		self.index = index

	def __repr__(self):
		return "RemoveOperation({})".format(self.index)

class MultiplyOperation:
	def __init__(self, index_a, index_b):
		self.type = OperationType.Multiply
		self.index_a = index_a
		self.index_b = index_b

	def __repr__(self):
		return "MultiplyOperation({}, {})".format(self.index_a, self.index_b)

def multiply_remaining(removed, n):
	"""
	Removed should be list of 1-based indices
	"""
	operations = []
	keep_indices = set(range(1, n + 1)) - set(removed)
	previous = None
	for index in sorted(keep_indices):
		if previous is not None:
			operations.append(MultiplyOperation(previous, index))
		previous = index
	return operations

def multiply_everything(n):
	operations = []
	for i in range(1, n):
		operations.append(MultiplyOperation(i, i + 1))
	return operations

def remove_indices_and_multiply_remaining(removed, n):
	"""
	Removed should be a collection of 1-based indices
	"""
	operations = []
	keep_indices = set(range(1, n + 1)) - set(removed)
	previous = None
	for index in sorted(keep_indices):
		if previous is not None:
			operations.append(MultiplyOperation(previous, index))
		previous = index
	return operations

def find_zero_indices(xs):
	"""
	Returns sorted list of 1-based indices
	"""
	zero_indices = []
	for index, x, in enumerate(xs):
		if x == 0:
			zero_indices.append(index + 1)
	return zero_indices

def remove_indices_and_multiply_remaining(indices_to_remove, n):
	"""
	indices_to_remove should be a sorted list of 1-based indices
	"""
	# multiply together indices to remove and then actually remove last one
	operations = []
	previous = None
	for index in indices_to_remove:
		if previous is not None:
			operations.append(MultiplyOperation(previous, index))
		previous = index
	
	if len(indices_to_remove) < n:
		operations.append(RemoveOperation(previous))
		operations += multiply_remaining(indices_to_remove, n)
	return operations

def find_index_of_largest_negative(xs):
	# or index of smallest absolute value negative
	# returns 1 based index
	maximum = float('-inf')
	maximum_index = None
	for index, x in enumerate(xs):
		if x < 0 and x > maximum:
			maximum = x
			maximum_index = index
	return maximum_index + 1

def solve(xs):
	"""
	Returns list of |xs| - 1 operations
	"""
	n = len(xs)
	# Count negatives and zeros
	negatives = 0
	zeros = 0
	for x in xs:
		if x == 0:
			zeros += 1
		if x < 0:
			negatives += 1
	
	if zeros == 0 and negatives == 0:
		# all positive so just multiply everything to maximize
		return multiply_everything(n)
	elif zeros == n:
		# can only be left with 0, multiply everything...
		return multiply_everything(n)
	elif zeros == 0 and negatives > 0:
		if negatives % 2 == 0:
			# multiply everything for largest positive number
			return multiply_everything(n)
		else:
			# get rid of smallest absolute value negative to be left with even number of negatives
			# then multiply everything for largest positive number
			return remove_indices_and_multiply_remaining([find_index_of_largest_negative(xs)], n)
	elif negatives == 0 and zeros > 0:
		return remove_indices_and_multiply_remaining(find_zero_indices(xs), n)
	else:#if zeros > 0 and negatives > 0
		if negatives % 2 == 0:
			# get rid of zeros and
			# multiply everything for largest positive number
			return remove_indices_and_multiply_remaining(find_zero_indices(xs), n)
		else:
			# get rid of zeros as well as smallest negative number
			# then multiply everything for largest positive number
			indices_to_remove = sorted([find_index_of_largest_negative(xs)] + find_zero_indices(xs))
			return remove_indices_and_multiply_remaining(indices_to_remove, n)

def verify(xs, maximum):
	solution = solve(xs)
	#print("solve(", xs, ") returned ", solution)

	assert len(solution) == len(xs) - 1

	num_removes = 0
	removed = [False] * len(xs)
	for operation in solution:
		if operation.type is OperationType.Remove:
			assert not removed[operation.index - 1]
			num_removes += 1
			removed[operation.index - 1] = True
		elif operation.type is OperationType.Multiply:
			assert not removed[operation.index_a - 1]
			assert not removed[operation.index_b - 1]
			removed[operation.index_a - 1] = True
			xs[operation.index_b - 1] *= xs[operation.index_a - 1]

	assert num_removes <= 1

	num_remaining = 0
	remaining_index = -1
	for index, value in enumerate(xs):
		if not removed[index]:
			num_remaining += 1
			remaining_index = index
		
	assert num_remaining == 1
	assert maximum == xs[remaining_index]

n = int(input())
xs = list(map(int, input().split()))[:n]
for operation in solve(xs):
	if operation.type is OperationType.Multiply:
		print(1, operation.index_a, operation.index_b)
	else:
		print(2, operation.index)

# verify([-1, -1, -1, -1, -1, -1], 1)
# verify([-1, -1, -1, -1, -1], 1)
# verify([-1, -1, -100, -1, -1], 100)
# verify([-100, -1, -1, -1, -1], 100)
# verify([0, 0], 0)
# verify([0, 0, 0], 0)
# verify([1, 2, 3], 6)
# verify([0, 2, 3], 6)
# verify([2, 0, 3], 6)
# verify([2, 1, 0, 3], 6)
# verify([2, 2, 0, 3], 12)
# verify([2, 2, 0, 0, 3], 12)
# verify([2, 2, 0, 0, 0, 3], 12)
# verify([0, 2, 2, 0, 0, 0, 3], 12)
# verify([2, 2, 0, 0, 0, 3], 12)
# verify([0, 2, 0, 2, 0, 0, 0, 3, 0], 12)
# verify([-1, 2, 3], 6)
# verify([2, -1, 3], 6)
# verify([2, 3, -100], 6)
# verify([2, 0, 3, -1, -100], 600)
# verify([2, 0, -1, -100, 3, -2, -2], 2400)
# verify([2, 0, -1, -100, 3, -2, -2, 0], 2400)
# verify([2, 0, -1, -100, 3, -2, -2, 0, 2], 4800)
# verify([0, -1, 5], 5)
# verify([0, -1, 0, 5], 5)
# verify([0, -1, 0, -100, 5], 500)
# verify([0, -2, 0, -100, -5, 5], 2500)
# verify([0, -10, 0, 0], 0)
# verify([0, -10, -10, 0], 100)

