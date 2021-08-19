from enum import Enum


class OperationType(Enum):
    Multiply = 1
    Remove = 2


class RemoveOperation:

    def __init__(self, index):
        self.type = OperationType.Remove
        self.index = index

    def __repr__(self):
        return 'RemoveOperation({})'.format(self.index)


class MultiplyOperation:

    def __init__(self, index_a, index_b):
        self.type = OperationType.Multiply
        self.index_a = index_a
        self.index_b = index_b

    def __repr__(self):
        return 'MultiplyOperation({}, {})'.format(self.index_a, self.index_b)


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
    for (index, x) in enumerate(xs):
        if x == 0:
            zero_indices.append(index + 1)
    return zero_indices


def remove_indices_and_multiply_remaining(indices_to_remove, n):
    """
    indices_to_remove should be a sorted list of 1-based indices
    """
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
    maximum = float('-inf')
    maximum_index = None
    for (index, x) in enumerate(xs):
        if x < 0 and x > maximum:
            maximum = x
            maximum_index = index
    return maximum_index + 1


def solve(xs):
    """
    Returns list of |xs| - 1 operations
    """
    n = len(xs)
    negatives = 0
    zeros = 0
    for x in xs:
        if x == 0:
            zeros += 1
        if x < 0:
            negatives += 1
    if zeros == 0 and negatives == 0:
        return multiply_everything(n)
    elif zeros == n:
        return multiply_everything(n)
    elif zeros == 0 and negatives > 0:
        if negatives % 2 == 0:
            return multiply_everything(n)
        else:
            return remove_indices_and_multiply_remaining([find_index_of_largest_negative(xs)], n)
    elif negatives == 0 and zeros > 0:
        return remove_indices_and_multiply_remaining(find_zero_indices(xs), n)
    elif negatives % 2 == 0:
        return remove_indices_and_multiply_remaining(find_zero_indices(xs), n)
    else:
        indices_to_remove = sorted([find_index_of_largest_negative(xs)] + find_zero_indices(xs))
        return remove_indices_and_multiply_remaining(indices_to_remove, n)


def verify(xs, maximum):
    solution = solve(xs)
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
    for (index, value) in enumerate(xs):
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
