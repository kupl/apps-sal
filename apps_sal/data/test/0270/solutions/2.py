import sys

n, m = list(map(int, input().split()))
links = [set() for _ in range(n)]
counts = [0] * n
for line in sys.stdin:
    s, t = list(map(int, line.split()))
    s -= 1
    t -= 1
    links[s].add(t)
    counts[s] += 1

# Expected number of edges passing from i to N
expected = [0.] * n
exp_get = expected.__getitem__

# i から伸びる辺を1本消すことで削減できる"iからNまでの辺数の期待値"の最大量
reducible = [0.] * n

for i in range(n - 2, -1, -1):
    nxt_exp = list(map(exp_get, links[i]))
    sum_exp = sum(nxt_exp)
    cnt = counts[i]

    expected[i] = sum_exp / cnt + 1

    if cnt > 1:
        reduced_exp = (sum_exp - max(nxt_exp)) / (cnt - 1) + 1
        reducible[i] = expected[i] - reduced_exp
    else:
        reducible[i] = 0.

# Probability of visiting i when starting from 1
probability = [0.] * n
probability[0] = 1.

rdc = 0.

for i in range(n - 1):
    fp = probability[i]
    jp = fp / counts[i]
    for j in links[i]:
        probability[j] += jp
    rdc = max(rdc, fp * reducible[i])

print((expected[0] - rdc))

