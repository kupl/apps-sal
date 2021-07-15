t = int(input())
for _ in range(t):
    n = int(input())
    first, last = 10**10, 0
    for i in range(n):
        l, r = [int(x) for x in input().split()]
        if r < first:
            first = r
        if l > last:
            last = l
    res = last - first
    if res >= 0:
        print(res)
    else:
        print(0)

