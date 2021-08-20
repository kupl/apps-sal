import bisect


def main(n, s, mod):
    ls = len(s)
    L = [[] for i in range(n + 1)]
    for (i, x) in enumerate(s):
        L[x].append(i)
    for i in range(1, ls + 1):
        for j in range(2 * i, n + 1, i):
            L[i] += L[j]
        L[i].sort()
    L = L[:ls + 1]
    counts = [list(range(ls)), [1 for i in range(ls)]]
    S = ls
    for d in range(2, ls + 1):
        if not L[d]:
            break
        lcounts = len(counts[0])
        sumcounts = [0]
        for i in range(1, lcounts + 1):
            sumcounts.append((sumcounts[i - 1] + counts[1][i - 1]) % mod)
        newcounts = [[], []]
        for x in L[d]:
            y = sumcounts[bisect.bisect_left(counts[0], x)]
            S = (S + y) % mod
            (newcounts[0].append(x), newcounts[1].append(y))
        counts = newcounts
    return S


useless = str(input()).split(' ')
s = [int(i) for i in input().split(' ')]
n = 10 ** 6
mod = 10 ** 9 + 7
print(main(n, s, mod))
