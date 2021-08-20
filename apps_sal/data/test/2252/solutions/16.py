(n, k) = map(int, input().split())
p = list(map(int, input().split()))


def solve():
    for i in range(k):
        (l, r, x) = map(int, input().split())
        (nrLarger, nrSmaller) = (r - x, x - l)
        (cL, cS) = (0, 0)
        if r == l:
            print('Yes')
        else:
            for j in range(l - 1, r):
                if p[j] < p[x - 1]:
                    cS += 1
                if cS > nrSmaller:
                    break
            print('Yes' if cS == nrSmaller else 'No')


solve()
