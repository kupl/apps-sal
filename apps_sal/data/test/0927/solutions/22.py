from collections import defaultdict

def f(a, b):
    for i in range(9,0,-1):
        if a[i] == b[i]: continue
        elif a[i] > b[i]:
            return True
        else:
            return False
    return False

N, M = map(int, input().split())
se = set()
A = list(map(int, input().split()))
toNum = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [[] for i in range(N+1)]
done = [False for i in range(N+10)]
done[N] = True
dics = [defaultdict(int) for i in range(N+1)]
for i in range(N-1, -1, -1):
    for a in A:
        num = toNum[a]
        if not done[i+num]: continue
        l = len(dp[i+num])+1
        d = dics[i+num].copy()
        d[a] += 1
        if l > len(dp[i]) or (l == len(dp[i]) and f(d, dics[i])):
            dp[i] = dp[i+num] + [a]
            done[i] = True
            dics[i] = d
dp[0].sort(reverse=True)
print(*dp[0], sep='')

