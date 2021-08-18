import sys
import itertools
import bisect
n, m = map(int, input().split())
w = list(map(int, input().split()))
lv = [map(int, input().split()) for _ in range(m)]
l, v = [list(i) for i in zip(*lv)]
#lv = [list(map(int, input().split())) for _ in range(m)]

if min(w) > min(v):
    print("-1")
    return

l = [i for _, i in sorted(zip(v, l))]
v.sort()

len_rm = list(itertools.accumulate(l, max))

ans = float("inf")
for W in itertools.permutations(w):
    length = [0] * n
    for i in range(n):
        w_ij = W[i]
        for j in range(i + 1, n):
            w_ij += W[j]
            idx = bisect.bisect_left(v, w_ij)
            if idx == 0:
                x_ij = 0
            else:
                x_ij = len_rm[idx - 1]
            length[j] = max(length[j], length[i] + x_ij)
            if idx == m:
                break
    ans = min(ans, length[-1])
print(ans)
