import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
M = [[] for i in range(m)]
for i in range(n):
    z = list(map(int, input().split()))
    for i in range(len(z)):
        M[i].append(z[i])

dp = [0 for i in range(n)]
dp[-1] = 1
for i in range(len(M)):

    x = M[i]
    temp = [0 for i in range(len(x))]
    temp[0] = 1
    for i in range(1, len(x)):
        if(x[i] >= x[i - 1]):
            temp[i] = 1
        else:
            temp[i] = 2
    re = [0 for i in range(len(temp))]
    re[-1] = 1
    for i in range(len(re) - 2, -1, -1):
        if(temp[i + 1] == 2):
            re[i] = 1
        else:
            re[i] = re[i + 1] + 1
    for i in range(len(dp)):
        dp[i] = max(dp[i], re[i])

r = int(input())
dp[-1] = 1

for i in range(r):
    l, r = list(map(int, input().split()))

    if(dp[l - 1] >= r - l + 1):
        print('Yes')
    else:
        print('No')
