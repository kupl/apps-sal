import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    P = list(map(int, input().split()))
    D = defaultdict(int)
    for num in range(n):
        D[P[num]] = num
    res = []
    used = set()
    for num in range(1, n + 1):
        idx = D[num]
        while idx + 1 != num:
            if idx + 1 > num:
                swap = P[idx - 1]
                if idx in used:
                    print(-1)
                    return
                P[idx - 1] = P[idx]
                P[idx] = swap
                used.add(idx)
                res.append(idx)
            else:
                swap = P[idx + 1]
                if idx + 2 in used:
                    print(-1)
                    return
                P[idx + 1] = P[idx]
                P[idx] = swap
                used.add(idx + 2)
                res.append(idx + 2)
            D[num] = D[swap]
            D[swap] = idx
            idx = D[num]
            if len(used) > n - 1:
                print(-1)
                return
    if len(res) != n - 1:
        print(-1)
        return
    print(*res, sep='\n')


def __starting_point():
    resolve()


__starting_point()
