n = int(input())
l = list(map(int, input().split()))
s = sum(l)
k = int(input())
for i in range(k):
	l, r = list(map(int, input().split()))
	if l <= s <= r:
		print(s)
		break
	elif l > s:
		print(l)
		break
else:
	print(-1)

