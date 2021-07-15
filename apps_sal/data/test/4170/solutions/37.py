n = int(input())
h = list(map(int,input().split()))
t = [0 for _ in range(n)]
memo = h[0]
for i in range(n-1):
	if memo >= h[i+1]:
		t[i+1] += t[i]+1
		memo = h[i+1]
	else:
		memo = h[i+1]
print(max(t))
