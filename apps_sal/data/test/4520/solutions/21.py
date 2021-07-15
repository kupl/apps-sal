import functools
from math import inf

class event:
	def __init__(self, x, type, index):
		self.x = x
		self.type = type
		self.i = index

def custom_sort(a, b):
	# if a.i == b.i:
	# 	if a.type == "s" and b.type == "e":
	# 		return -1
	# 	if a.type == "e" and b.type == "s":
	# 		return 1
	if a.x < b.x:
		return - 1
	if a.x > b.x:
		return 1
	if a.type == "e" and b.type == "s":
		return 1
	if a.type == "s" and b.type == "e":
		return -1
	return 0

def __starting_point():
	line = input().split(" ")
	n, k = int(line[0]), int(line[1])

	events = []
	original_events = []
	for i in range(n):
		line = input().split(" ")
		s = int(line[0])
		e = int(line[1])

		events.append(event(s, "s", i))
		events.append(event(e, "e", i))
		original_events.append([s, e])

	events.sort(key=functools.cmp_to_key(custom_sort))

	active = {}
	ans = []

	cnt = 0
	for curr in events:
		# print(curr.x, curr.type, curr.i, cnt)
		if curr.type == "s":
			cnt += 1
			active[curr.i] = 1

			if cnt > k:
				# print("over:", curr.i, cnt)
				to_remove = 0
				rightmost = -inf
				for i in active.keys():
					if original_events[i][1] > rightmost:
						rightmost = original_events[i][1]
						to_remove = i
				ans.append(str(to_remove + 1))
				del active[to_remove]
				cnt -= 1

		else:
			if curr.i in active.keys():
				cnt -= 1
				del active[curr.i]

	print(len(ans))
	print(" ".join(ans))
__starting_point()
