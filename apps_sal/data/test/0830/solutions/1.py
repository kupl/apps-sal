(n, k) = list(map(int, input().split(' ')))
t = list(map(int, input().split(' ')))
inst = max(t) - min(t)
i = 0
steps = []
while inst > 0 and i < k:
    imax = t.index(max(t))
    imin = t.index(min(t))
    steps.append(imax + 1)
    steps.append(imin + 1)
    t[imax] -= 1
    t[imin] += 1
    inst = max(t) - min(t)
    i += 1
print(inst, i)
for i in range(0, len(steps), 2):
    print(steps[i], steps[i + 1])
