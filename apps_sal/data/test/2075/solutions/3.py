def ij(s):
    i = 0
    j = 0
    for c in s:
        if c == ')':
            if j > 0:
                j -= 1
            else:
                i += 1
        else:
            j += 1
    return (i, j)


K = 10 ** 9 + 7


def ways(n, s):
    (I, J) = ij(s)
    f = n - len(s) - I - J
    if f < 0 or f % 2:
        return 0
    E = f // 2
    if E == 0:
        return 1
    C = [1]
    for n in range(E + max(I, J) + 1):
        C.append(C[n] * 2 * (2 * n + 1) // (n + 2))
    W = [[c % K for c in C]]
    W.append(W[0][1:])
    for i in range(2, E + max(I, J) + 1):
        W.append([(W[i - 1][e + 1] - W[i - 2][e + 1]) % K for e in range(E + max(I, J) + 1 - i + 1)])
    result = sum((W[I + k][e - k] * W[J + k][E - e] % K for k in range(E + 1) for e in range(k, E + 1)))
    return result


def __starting_point():
    (n, m) = list(map(int, input().split()))
    s = input()
    print(ways(n, s) % K)


__starting_point()
