import math


def gns():
    return list(map(int, input().split()))


t = 1
for i in range(t):
    n = int(input())
    ns = gns()
    ns.sort()
    nd = 1
    ans = 0
    for i in range(n):
        n = ns[i]
        if n - 1 >= nd:
            ans += 1
            nd = n
        elif n == nd:
            ans += 1
            nd = n + 1
        elif n + 1 == nd:
            ans += 1
            nd = n + 2
        else:
            continue
    print(ans)
