def solve():
    import numpy as np
    n = int(input())
    oc = [[] for _ in range(n)]
    prof = [[] for _ in range(n)]

    for i in range(n):
        oc[i] = list(map(int, input().split()))
    for i in range(n):
        prof[i] = list(map(int, input().split()))

    oc = np.array(oc)
    prof = np.array(prof)

    ans = -9999999999

    for a in range(1, 1 << 10):
        res = np.zeros(n, dtype=np.int64)
        for b in range(10):
            if a >> b & 1:
                res += oc[:, b]
        #print(res)
        tmp = 0
        for i, x in enumerate(res):
            tmp += prof[i, x]
        #print(tmp)
        ans = max(ans, tmp)
    print(ans)


solve()

