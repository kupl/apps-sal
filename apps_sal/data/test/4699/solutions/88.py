def minN(N: int, usable: list, restrict=True):
    usable.sort()
    keta = False
    if restrict:
        for i in usable:
            if i >= N:
                return str(i)
        return '1' + str(usable[0])
    else:
        return str(usable[0])


def rote(N: list, D: set, d: set):
    ans = []
    flag = True
    lenNstr = len(N)
    for (i, n) in enumerate(N):
        n = int(n)
        keta = 10 ** (len(N) - i - 1)
        if flag:
            if n in D:
                ans.append(int(minN(n, d)) * keta)
                flag = False
            else:
                ans.append(keta * n)
        else:
            ans.append(keta * min(d))
    return sum(ans)


def main():
    (N, K) = list(map(int, input().split()))
    D = set(map(int, input().split()))
    numset = set(range(0, 10))
    d = list(numset.difference(D))
    d.sort()
    for _ in range(10):
        Nstr = list(str(N))
        ans = rote(Nstr, D, d)
        N = ans
    print(ans)


def __starting_point():
    main()


__starting_point()
