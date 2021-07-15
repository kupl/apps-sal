N = int(input())
W = list(map(int, input().split()))

tot = sum(W)
res = tot
s = 0
for i in range(N-1):
    s += W[i]
    res = min(res, abs(tot - 2 * s))

print(res)
