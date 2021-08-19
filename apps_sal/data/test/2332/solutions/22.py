(n, k, m) = [int(x) for x in input().split()]
w = [x for x in input().split()]
a = [int(x) for x in input().split()]
cost = {w[i]: a[i] for i in range(n)}
group = {}
minis = []
for i in range(k):
    inp = [int(x) - 1 for x in input().split()]
    mini = 10000000000
    mini_w = None
    for j in range(1, inp[0] + 2):
        if cost[w[inp[j]]] < mini:
            mini_w = cost[w[inp[j]]]
            mini = cost[w[inp[j]]]
        group[w[inp[j]]] = i
    minis.append(mini_w)
letter = [x for x in input().split()]
summa = 0
for wor in letter:
    summa += minis[group[wor]]
print(summa)
