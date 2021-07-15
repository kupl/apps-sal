def f(i, a):
	used = [False] * n
	while not used[i]:
		used[i] = True
		i = a[i] - 1
	return i
	

n = int(input())
a = [int(i) for i in input().split()]
for i in range(n):
	print(f(i, a) + 1, end = ' ')
