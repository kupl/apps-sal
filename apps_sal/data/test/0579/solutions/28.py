from itertools import accumulate


def solve(n, k, ppp, ccc):
    NINF = -(10 ** 18)
    ans = NINF

    checked = [False] * n
    for s in range(n):
        if checked[s] == True:
            continue
        checked[s] = True
        scores = [ccc[ppp[s]]]
        v = ppp[s]
        while v != s:
            scores.append(ccc[ppp[v]])
            checked[v] = True
            v = ppp[v]

        l = len(scores)
        d, m = divmod(k, l)
        loop = sum(scores)

        if d > 0:
            d -= 1
            m += l

        scores += scores * 2
        scores.insert(0, 0)
        acc = list(accumulate(scores))
        tmp = max(max(acc[i + 1:i + m + 1]) - acc[i] for i in range(l))
        ans = max(ans, tmp, loop * d + tmp)

    return ans


n, k = list(map(int, input().split()))
ppp = list(map(int, input().split()))
ppp = [p - 1 for p in ppp]
ccc = list(map(int, input().split()))

print((solve(n, k, ppp, ccc)))

