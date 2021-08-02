import sys
readline = sys.stdin.readline
h, w, d = map(int, readline().split())
A = [list(map(int, readline().split())) for _ in range(h)]
q = int(readline())
LR = [tuple(map(lambda x:int(x) - 1, readline().split())) for _ in range(q)]

D = dict()
for hi in range(h):
    for wi in range(w):
        D[A[hi][wi] - 1] = [hi, wi]

DP = [0] * (h * w)
for i in range(d, h * w):
    px, py = D[i - d]
    x, y = D[i]
    DP[i] = DP[i - d] + abs(x - px) + abs(y - py)

for l, r in LR:
    print(DP[r] - DP[l])
