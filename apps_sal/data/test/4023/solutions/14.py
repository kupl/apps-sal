import sys
sys.setrecursionlimit(3000)

n = int(input())
a = list(map(int, input().split()))
M = max(a)
m = min(a)
a = list([x - m for x in a])

def build(begin, target):
	stack = []
	nonlocal n, a
	i = begin
	currenth = a[begin]
	# print(a, currenth)
	while i < n:
		while i + 1 < n and a[i + 1] == currenth:
			i += 1
		if i == n - 1:
			if not stack:
				return i
			elif (i - begin + 1) % 2 != 0 and a[i] != target:
				return -1
			else:
				target, currenth, begin = stack.pop()
		elif a[i + 1] > currenth:
			if (i - begin + 1) % 2 != 0:
				return -1
			elif a[i + 1] >= target:
				if not stack:
					return i
				else:
					target, currenth, begin = stack.pop()
			else:
				currenth = a[i + 1]
				i += 1
		else: # a[i + 1] < currenth
			stack.append((target, currenth, begin))
			# print(stack, i)
			i += 1
			target = currenth
			currenth = a[i]
			begin = i

res = build(0, M)
# print(res)
while res != -1 and res < n - 1:
	res = build(res + 1, M)
	print(res)
if res == n - 1:
	print('YES')
else:
	# print(build(0, M))
	print('NO')

