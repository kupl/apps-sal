import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n = int(input())
p = list(map(int, input().split()))
odd = (n + 1) // 2
even = n - odd
for i in p:
    if i:
        if i % 2 == 0:
            even -= 1
        else:
            odd -= 1

if even == 0:
    p = [i if i else 1 for i in p]
if odd * even == 0:
    ans = 0
    prev = p[0]
    for pi in p:
        ans += (pi + prev) % 2
        prev = pi
    print(ans)
    return

DP = [[float("inf")] * (even + 1) for i in range(2)]
for i in range(n):
    nxt = [[float("inf")] * (even + 1) for i in range(2)]
    if i == 0:
        if p[i]:
            if p[i] % 2 == 0:
                nxt[0][0] = 0
            else:
                nxt[1][0] = 0
        else:
            nxt[0][1] = 0
            nxt[1][0] = 0
    else:
        if p[i]:
            if p[i] % 2 == 0:
                for j in range(even + 1):
                    nxt[0][j] = min(DP[0][j], DP[1][j] + 1)
            else:
                for j in range(even + 1):
                    nxt[1][j] = min(DP[0][j] + 1, DP[1][j])
        else:
            for j in range(1, even + 1):
                nxt[0][j] = min(DP[0][j - 1], DP[1][j - 1] + 1)
            for j in range(even + 1):
                nxt[1][j] = min(DP[0][j] + 1, DP[1][j])
    DP = nxt
print(min(DP[0][-1], DP[1][-1]))
