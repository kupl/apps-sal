n = int(input())
a = list(map(int, input().split()))
a.sort()
s = 0
for i in range(n // 2):
	s += a[2 * i + 1] - a[2 * i]
print(s)


