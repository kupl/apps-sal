n,k = list(map(int,input().split()))
ans1, ans2 = 0, 0

if(k != 0 and k != n):
	ans1 = 1
if(3*k < n):
	ans2 = 2*k
else:
	ans2 = n-k

print(ans1, ans2)

