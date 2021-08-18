

from collections import defaultdict
N, C = list(map(int, input().split()))
D = defaultdict(int)
t = defaultdict(int)

for i in range(C):
    s = list(map(int, input().split()))
    for j in range(C):
        D[(i, j)] = s[j]
for i in range(N):
    s = list(map(int, input().split()))
    for j in range(N):
        t[((i + j) % 3, s[j] - 1)] += 1
ans = 1 << 30
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i != j != k != i:
                res = 0
                for l in range(C):
                    res += D[(l, i)] * t[(0, l)]
                for l in range(C):
                    res += D[(l, j)] * t[(1, l)]
                for l in range(C):
                    res += D[(l, k)] * t[(2, l)]
                ans = min(ans, res)


print(ans)
