D, G = map(int, input().split())

P = []
C = []

for i in range(D):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c)

ans = 1000
for i in range(2**D):
    point = 0
    num = 0
    unsolved = []
    for j in range(D):
        if (i >> j) & 1 == 1:
            point += 100 * (j + 1) * P[j] + C[j]
            num += P[j]

        else:
            unsolved.append(j)

    if G <= point:
        ans = min(num, ans)

    else:
        l = []
        unsolved.reverse()
        for i in unsolved:
            l += [100 * (i + 1)] * (P[i] - 1)
        for j in range(len(l)):
            point += l[j]
            num += 1

            if G <= point:
                ans = min(num, ans)
print(ans)
