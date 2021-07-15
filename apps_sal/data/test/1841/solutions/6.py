n,m = map(int,input().split())
a = list (map(int,input().split()))
s = set([])
ans = [0]*n
for i in reversed(range(n)):
	if (not a[i] in s): s.add(a[i])
	ans[i] = len(s)
for i in range(m):
	z = int(input())
	print (ans[z-1])
