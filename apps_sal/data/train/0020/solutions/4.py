def solve():
    n, m = list(map(int, input().split()))
    cust = []
    for ___ in range(n):
        t, l, h = list(map(int, input().split()))
        cust.append((t, l, h))

    cust.sort()

    lastT = 0
    lastMaxT = m
    lastMinT = m

    for t, l, h in cust:
        nextMax = lastMaxT + t - lastT
        nextMin = lastMinT - t + lastT

        if nextMax < l or nextMin > h:
            print("NO")
            return

        lastMaxT = min(h, nextMax)
        lastMinT = max(l, nextMin)
        lastT = t
    print("YES")


q = int(input())
for __ in range(q):
    solve()

