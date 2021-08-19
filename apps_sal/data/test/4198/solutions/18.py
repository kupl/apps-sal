(A, B, X) = map(int, input().split())
Nmax = 10 ** 9
Nmin = 1
Nmid = (Nmax + Nmin) // 2


def nIsAffordable(a, b, n):
    lenOfN = len(str(n))
    price = a * n + b * lenOfN
    if price <= X:
        return True
    else:
        return False


if nIsAffordable(A, B, Nmax):
    print(Nmax)
else:
    while Nmax != Nmin:
        if nIsAffordable(A, B, Nmid):
            Nmin = Nmid + 1
            Nmid = (Nmax + Nmin) // 2
        else:
            Nmax = Nmid
            Nmid = (Nmax + Nmin) // 2
    print(Nmid - 1)
