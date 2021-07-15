import collections

def __starting_point():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    p = 0
    d = collections.Counter()
    d[0] = 1
    limit = 1 << (k-1)
    mask = (1 << k) - 1
    for i in range(n):
        p ^= min(a[i], mask-a[i])
        d[p] += 1

    res = 0
    for key in d:
        i = d[key] // 2
        j = d[key] - i
        res += (i-1)*i//2 + (j-1)*j//2
    res = n*(n+1)//2 - res
    print(res)
__starting_point()
