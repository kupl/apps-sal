
n,m = map(int, input().split())

mx = 1e11
for i in range(n):
	a,b = map(int, input().split())
	mx = min(mx, m*a/b)
print (mx)
