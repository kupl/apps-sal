from bisect import bisect_right


def R():
    return map(int, input().split())


f = open('input.txt', 'r')
n = int(f.readline())
L = sorted(map(int, f.readline().split()))
res = 10 ** 9
for i in range(n):
    k = bisect_right(L, 2 * L[i])
    if k == n:
        res = min(res, i)
        break
    res = min(res, i + n - k)
open('output.txt', 'w').write(str(res))
