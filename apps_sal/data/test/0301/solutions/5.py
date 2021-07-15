x, s = map(int, input().split())
if x > s:
	print(-1)
elif (s-x) % 2 == 1:
	print(-1)
elif s == 0:
	print(0)
elif s == x:
	print(1)
	print(s)
else:
	if (x | (s-x>>1)) == x + (s-x>>1):
		print(2)
		print(x + (s-x>>1), s-x>>1)
	else:
		print(3)
		print(x, s-x>>1, s-x>>1)
