n = int(input())
l = [int(x) for x in input().split()]
l.reverse()
for i in range(1, n):
	if l[i] > l[i - 1]:
		print(n - i)
		return
print(0)

