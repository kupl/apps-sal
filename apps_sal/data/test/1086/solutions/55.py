import sys
input = sys.stdin.readline
h,w = list(map(int,input().split()))
la = [list(map(int,input().split())) for i in range(h)]
for i in range(h):
    l = list(map(int,input().split()))
    for j,num in enumerate(l):
        la[i][j] = abs(la[i][j]-num)
dp = [[0 for i in range(w)] for j in range(h)]
k = (h+w)*80+2
dp[0][0] = 1 << (k+la[0][0]) | 1 << (k-la[0][0])

for i in range(h):
    for j in range(w):
        if i:
            dp[i][j] |= (dp[i-1][j] << la[i][j]) | dp[i-1][j] >> la[i][j]
        if j:
            dp[i][j] |= (dp[i][j-1] << la[i][j]) | dp[i][j-1] >> la[i][j]

check = dp[-1][-1]       
for i in range(k):
    if (check >> k+i) & 1 or (check >> k-i) & 1:
        print(i)
        return

