import numpy as np

def solve(n, k, aaa, fff):
    aaa = np.sort(aaa)
    fff = np.sort(fff)[::-1]

    l = -1
    r = 1e12
    while l+1 < r:
        c = (l+r)//2
        s = np.clip(aaa - c//fff, 0, None).sum()
        if s <= k:
            r = c
        else:
            l = c
    return int(r)


n, k = map(int, input().split())
aaa = np.array(list(map(int, input().split())), dtype=np.int64)
fff = np.array(list(map(int, input().split())), dtype=np.int64)

print(solve(n, k, aaa, fff))
