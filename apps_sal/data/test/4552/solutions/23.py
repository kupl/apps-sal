def solve():
    import numpy as np
    n = int(input())
    oc = [list(map(int, input().split())) for _ in range(n)]
    prof = [list(map(int, input().split())) for _ in range(n)]

    oc = np.array(oc)
    prof = np.array(prof)

    inf = 10 ** 10
    ans = - inf

    for a in range(1, 1 << 10):
        res = np.zeros(n, dtype=np.int64)
        for b in range(10):
            if a >> b & 1:
                res += oc[:, b]
        tmp = 0
        for i, x in enumerate(res):
            tmp += prof[i, x]
        ans = max(ans, tmp)
    print(ans)


solve()


