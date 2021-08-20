import numpy as np
(n, k) = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
(cycles, check) = ([], [False] * n)
for pi in p:
    if not check[pi - 1]:
        (curr, cycle) = (pi, [])
        check[pi - 1] = True
        while pi != p[curr - 1]:
            check[curr - 1] = True
            cycle.append(c[curr - 1])
            curr = p[curr - 1]
        check[curr - 1] = True
        cycles.append(cycle + [c[curr - 1]])
scores = []
for cycle in (np.array(cycle) for cycle in cycles):
    for i in range(cycle.size):
        cum = np.roll(cycle, i).cumsum()
        if cum[-1] > 0 and k > cycle.size:
            scores.append(cum[-1] * (k // cycle.size - 1) + np.concatenate([cum, cum[:k % cycle.size] + cum[-1]]).max())
        else:
            scores.append(cum[:min(k, cum.size)].max())
print(max(scores))
