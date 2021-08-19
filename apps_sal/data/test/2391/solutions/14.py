n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
f = [0] * n
g = [0] * n
for i in range(n):
    f[i] = a[i] ^ a[(i + 1) % n]
    g[i] = b[i] ^ b[(i + 1) % n]


def KMP(S, W):
    (ls, lw) = (len(S), len(W))
    (m, i) = (0, 0)
    T = _KMP_table(W)
    res = list()
    while m + i < ls:
        if W[i] == S[m + i]:
            i += 1
            if i == lw:
                res.append(m)
                m += i - T[i]
                if i > 0:
                    i = T[i]
        else:
            m += i - T[i]
            if i > 0:
                i = T[i]
    return res


def _KMP_table(W):
    W += ['$']
    lw = len(W)
    T = [0] * lw
    T[0] = -1
    (i, j) = (2, 0)
    while i < lw:
        if W[i - 1] == W[j]:
            T[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = T[j]
        else:
            T[i] = 0
            i += 1
    return T


res = KMP(f * 2, g)
for x in res:
    if x < n:
        print(x, a[x] ^ b[0])
