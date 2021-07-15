from collections import defaultdict

n = int(input())
al = list(map(int, input().split()))

dp = defaultdict(lambda: -10**18)
dp[(0,0,False)] = 0

for i in range(n):
    for j in range(i//2-1,i//2+2):
        dp[(i+1,j,False)] = max(
            dp[(i,j,False)],
            dp[(i,j,True)]
        )
        dp[(i+1,j,True)] = dp[(i,j-1,False)] + al[i]

print((max(
    dp[(n,n//2,False)],
    dp[(n,n//2,True)]
)))

