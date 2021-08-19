def main():
    from functools import lru_cache
    import bisect
    S = input()
    T = input()
    if set(S) & set(T) != set(T):
        print(-1)
    else:
        lt = len(T)
        ls = len(S)
        st = set(T)
        D = dict()
        for t in st:
            D[t] = list()
            for (i, s) in enumerate(S):
                if t == s:
                    D[t].append(i)
        pre = -1
        cnt = 0

        @lru_cache(maxsize=None)
        def judge(pre, t):
            X = D[t]
            index = bisect.bisect(X, pre)
            if len(X) == index:
                return (X[0], True)
            else:
                return (X[index], False)
        for t in T:
            J = judge(pre, t)
            pre = J[0]
            if J[1]:
                cnt += 1
        print(cnt * len(S) + pre + 1)


def __starting_point():
    main()


__starting_point()
