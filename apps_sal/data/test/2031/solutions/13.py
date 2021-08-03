def min_s(a, k):
    res = a.copy()
    for i in range(len(a) - k):
        m = min(res)
        res.reverse()
        res.remove(m)
        res.reverse()

    return res


n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
for _ in range(m):
    k, pos = [int(x) for x in input().split()]

    l = min_s(a, k)

    print(l[pos - 1])
