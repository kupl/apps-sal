import sys


def bestval(pp, cc):
    k = len(pp)
    k_2 = k // 2 + 1
    for f in range(1, k_2):
        if k % f == 0:
            for offs in range(f):
                good = True
                num = cc[offs]
                upp = k // f // 2 + 1
                for j in range(1, upp):
                    v1 = f * j
                    v2 = k - v1 + offs
                    v1 += offs
                    if cc[v1] != num or cc[v2] != num:
                        good = False
                        break
                if good:
                    return f
    return k


for q in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    p = [int(j) - 1 for j in sys.stdin.readline().split()]
    c = [int(j) - 1 for j in sys.stdin.readline().split()]
    fnd = [0] * n
    ans = n + 1
    for i in range(n):
        if not fnd[i]:
            ppp = [i]
            ccc = [c[i]]
            fnd[i] = 1
            j = p[i]
            while j != i:
                fnd[j] = 1
                ppp.append(j)
                ccc.append(c[j])
                j = p[j]
            ans = min(ans, bestval(ppp, ccc))
    sys.stdout.write(str(ans) + '\n')
