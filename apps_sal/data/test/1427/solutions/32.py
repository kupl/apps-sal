def main():
    import copy
    n = int(input())
    a = list(map(int, input().split()))
    A = copy.deepcopy(a)
    mod = 10 ** 9 + 7
    l = {}
    for i in range(n):
        for j in range(2, int(a[i] ** 0.5) + 1):
            if a[i] % j == 0:
                cnt = 0
                while a[i] % j == 0:
                    cnt += 1
                    a[i] = a[i] // j
                if l.get(j) == None:
                    l[j] = cnt
                else:
                    l[j] = max(cnt, l[j])
        if a[i] != 1:
            if l.get(a[i]) == None:
                l[a[i]] = 1
    L = 1
    for k in list(l.keys()):
        L *= pow(k, l[k], mod)
    L = L % mod
    ans = 0
    for i in range(n):
        ans += L * pow(A[i], mod - 2, mod) % mod
        ans = ans % mod
    print(ans)


def __starting_point():
    main()


__starting_point()
