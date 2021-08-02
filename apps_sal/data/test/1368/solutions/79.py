from heapq import heappop, heapify, heappush
import sys
INF = 10 ** 7
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

fac = [1, 1]
for i in range(2, 51):
    fac.append(fac[-1] * i)


def nck(n, k):
    return fac[n] // fac[n - k] // fac[k]


def main():
    n, a, b = list(map(int, input().split()))
    v = list(map(int, input().split()))

    v.sort(reverse=True)
    tot = sum(v[:a])
    cnt = a

    ok = 0
    change = 0
    for i in range(a, n):
        if v[i] * cnt == tot:
            ok += 1
        elif v[i] == v[a - 1]:
            change += 1

    same = 1
    for i in range(a - 2, -1, -1):
        if v[i] == v[a - 1]:
            same += 1

    ans = 0
    if ok > 0:
        for i in range(same, b - a + same + 1):
            ans += nck(same + ok, i)
    elif change > 0:
        ans += nck(same + change, same)
    else:
        ans += 1

    print((tot / cnt))
    print(ans)


def __starting_point():
    main()


__starting_point()
