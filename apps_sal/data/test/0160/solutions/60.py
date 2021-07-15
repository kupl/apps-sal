N, K = (int(i) for i in input().split())
A = [int(i) for i in input().split()]

def yaku(N):
    res = []
    for i in range(1, round(N**(1/2)) + 3 ):
        if N%i == 0:
            res.append(i)

    res2 = [N//i for i in res]
    res = list(set(res + res2))
    return res

ys = yaku(sum(A))
ys.sort(reverse=True)
for y in ys:
    M = [a%y for a in A if a%y]
    ma = 0
    mi = y*len(M) - sum(M)
    M.sort()
    for m in M:
        ma += m
        mi -= (y - m)
        if ma == mi:
            break
    if ma <= K:
        print(y)
        return

