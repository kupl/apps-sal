n = int(input())
s = list(map(int, input().split()))
x = sum(s)
if x % 2 == 1:
	print("NO")
else:
	for c in s:
		if c > x - c:
			print("NO")
			return
	print("YES")

