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

expected = [0.] * n
exp_get = expected.__getitem__

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

probability = [0.] * n
probability[0] = 1.

for i in range(n - 1):
    jp = probability[i] / counts[i]
    for j in links[i]:
        probability[j] += jp

print((expected[0] - max(p * r for p, r in zip(probability, reducible))))
