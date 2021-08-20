from collections import Counter


def nCr(n, r):
    t = 1
    for i in range(n - r + 1, n + 1):
        t *= i
    for i in range(2, r + 1):
        t //= i
    return t


def main():
    (N, A, B) = list(map(int, input().split()))
    V = list(map(int, input().split()))
    VV = Counter(V)
    m = 0
    c = 0
    for v in sorted(list(VV.keys()), reverse=True):
        vc = VV[v]
        if c + vc <= A:
            m += v * vc
            c += vc
            continue
        break
    else:
        print(m / c)
        print(1)
        return
    min_c = A - c
    max_c = min(B - c, vc)
    m += v * min_c
    c += min_c
    print(m / c)
    if m != c * v:
        max_c = min_c
    r = 0
    for i in range(min_c, max_c + 1):
        r += nCr(vc, i)
    print(r)


main()
