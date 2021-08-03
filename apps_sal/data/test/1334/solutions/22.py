def solve():
    n, k = list(map(int, input().split()))
    S = input()
    L = list(set(list(map(ord, S))))
    L.sort()

    I = {}
    for i, l in enumerate(L):
        I[l] = i

    first = L[0]
    last = L[-1]

    res = ""
    if k > n:
        res += S
        res += chr(first) * (k - n)
        print(res)
        return
    else:
        for i in reversed(list(range(k))):
            if ord(S[i]) < last:
                remained = L[I[ord(S[i])] + 1]
                res += S[:i]
                res += chr(remained)
                res += chr(first) * (k - i - 1)
                print(res)
                return


def __starting_point():
    solve()


__starting_point()
