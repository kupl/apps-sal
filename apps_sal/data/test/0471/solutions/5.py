n, a = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]
s.sort()
t = len(s)-1
for i in range(n):
	if s[i] >a:
		t = i-1
		break
if n == 1:
	print(0)
elif t == -1:
	print(abs(s[-2]-a))
elif t == n-1:
	print(abs(a-s[1]))
elif t == 0:
	print(min(abs(s[-1]-a), abs(s[-2]-s[0]+a-s[0]), abs(s[-2]-s[0]+s[-2]-a)))
elif t == n-2:
	print(min(abs(a-s[0]), abs(s[-1]-s[1]+s[-1]-a), abs(s[-1]-s[1]+a-s[1])))
else:
	ans = min(abs(s[-1]-s[1]+a-s[1]),abs(s[-1]-s[1]+s[-1]-a), abs(s[-2]-s[0]+a-s[0]), abs(s[-2]-s[0]+s[-2]-a))
	print(ans)


