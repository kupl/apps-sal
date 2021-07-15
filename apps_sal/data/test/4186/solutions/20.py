#codeforces _10892B_live
gi = lambda : list(map(int,input().split()))
n, = gi()
l = gi()
ans = 0
l.sort()
for k in range(0,n,2):
	ans += l[k+1] - l[k]
print(ans)
