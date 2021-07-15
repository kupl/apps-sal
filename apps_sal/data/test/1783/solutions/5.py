m,n = list(map(int,input().split()))
arr = [int(x) for x in input().split()]
s = sum(arr[:n])
val = m-n+1
ns = s/val
for i in range(n,m):
	s = s + arr[i] - arr[i-n]
	ns += s/val
print(ns)

