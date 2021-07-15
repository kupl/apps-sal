n = int(input())
P = list(map(int, input().split()))
X = list(map(int, input().split()))

dp = [0]*n
child = [[] for i in range(n)]
for i in range(n-1):
    child[P[i]-1].append(i+1)

for i in range(n-1, -1, -1):
    if not child[i]:
        dp[i] = 0
    else:
        su = 0
        re = 0
        for c in child[i]:
            z = min(X[c], dp[c])
            su += z
        if su > X[i]:
            print("IMPOSSIBLE")
            return
        can = X[i] - su
        ss = set([0])
        for c in child[i]:
            z = min(X[c], dp[c])
            rest = max(X[c], dp[c]) - z
            re += rest
            pp = set(ss)
            for s in ss:
                if s + rest <= can:
                    pp.add(s + rest)
            ss = pp
        dp[i] = su + re - max(ss)
print("POSSIBLE")

