def solve():
    N = int(input())
    Ss = input().rstrip()

    def isOK(L):
        setCand = set()
        RHs = []
        for i in range(N - L + 1):
            RH = hash(Ss[i:i + L])
            RHs.append(RH)
            if i - L >= 0:
                setCand.add(RHs[i - L])
            if RH in setCand:
                return True
        return False

    ng, ok = N // 2 + 1, 0
    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid

    print(ok)


solve()
