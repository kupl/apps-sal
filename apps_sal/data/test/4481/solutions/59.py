n = int(input())
L = list((input() for _ in range(n)))
D = dict.fromkeys(set(L), 0)
for l in L:
    D[l] += 1
m = max(D.values())
SD = sorted(D.items(), key=lambda x: x[0])
for (k, v) in SD:
    if v == m:
        print(k)
