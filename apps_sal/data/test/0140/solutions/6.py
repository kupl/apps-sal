def dp(ind, max_covered):
	max_covered = min(m, max_covered)

	if ind not in cache:
		cache[ind] = {}

	d = cache[ind]
	if max_covered in d:
		return d[max_covered]

	ans = blah(ind, max_covered)

	d[max_covered] = ans
	return ans


# path = {}

class Node:
	def __init__(self, key, val, next=None):
		self.key = key
		self.val = val
		self.next = next

def blah(ind, max_covered):
	x, s = antenna[ind]
	# key = (ind, max_covered)

	if max_covered >= m:
		# path[key] = Node(key, 0)
		return 0

	if ind == len(antenna) - 1:
		if max_covered < x - s - 1:
			left_needed = x - s - (max_covered + 1)
			right_needed = max(m - (x + s), 0)
			ans = max(left_needed, right_needed)
			# path[key] = Node(key, ans)
			return ans
		else:
			right_boundary = max(max_covered, x + s)
			ans = max(0, m - right_boundary)
			# path[key] = Node(key, ans)
			return ans

	if max_covered < x - s - 1:
		num_needed = x - s - (max_covered + 1)
		new_boundary = min(x + s + num_needed, m)
		use_i = num_needed + dp(ind + 1, new_boundary)
		dont_use_i = dp(ind + 1, max_covered)

		# if use_i < dont_use_i:
		# 	path[key] = Node(key, num_needed, path[(ind + 1, new_boundary)])
		# else:
		# 	path[key] = Node(key, 0, path[(ind + 1, max_covered)])

		return min(use_i, dont_use_i)
	else:
		new_boundary = min(max(max_covered, x + s), m)
		ans = dp(ind + 1, new_boundary)
		# path[key] = Node(key, 0, path[(ind + 1, new_boundary)])
		return ans

import sys

cache = {}


n, m = [int(x) for x in sys.stdin.readline().split(" ")]

antenna = []

for i in range(n):
	x, s = [int(x) for x in sys.stdin.readline().split(" ")]

	antenna.append((x, s))

antenna.sort(key=lambda a: a[0])

print(dp(0, 0))

