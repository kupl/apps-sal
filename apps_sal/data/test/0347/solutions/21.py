xs = [500, 1000, 1500, 2000, 2500]
ms = [int(x) for x in input().split()]
ws = [int(x) for x in input().split()]
hacks = [int(x) for x in input().split()]

res = 0
for i in range(len(xs)):
    problem = max(0.3 * xs[i], (1 - ms[i] / 250) * xs[i] - 50 * ws[i])
    res += problem

res += 100 * hacks[0] - 50 * hacks[1]
print(int(res))
