n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(n):
	s += a[i]
if (s == n - 1 and n > 1 or s == 1 and n == 1):
	print("YES")
else:
	print("NO")
