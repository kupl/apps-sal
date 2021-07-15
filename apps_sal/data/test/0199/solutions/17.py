n,s = map(int,input().split())
l = list(map(int, input().split()))

if sum(l) < s:
	print(-1)
	return
q = sum(l) - min(l) * n
if q>=s:
	print(min(l))
	return
print(min(l)-(s-q+n-1)//n)
