n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))

maxv = [0]
for _t, _v in zip(t, v):
    maxv[-1] = min(maxv[-1], _v)
    for ti in range(_t * 2):
        maxv.append(_v)

N = len(maxv)
candv = [0] * N
for i in range(N - 1):
    candv[i + 1] = min(candv[i] + 0.5, maxv[i + 1])

candv[-1] = 0
for i in reversed(list(range(1, N))):
    candv[i - 1] = min(candv[i - 1], candv[i] + 0.5)

ans = 0
for x1, x2 in zip(candv, candv[1:]):
    ans += (x1 + x2) * 0.5 / 2

print(ans)
