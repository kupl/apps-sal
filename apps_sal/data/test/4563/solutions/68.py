import math

n = int(input())
ans = list(map(int, input().split()))
if n == 1:
    print((sum(ans)))

else:
    ans1 = []
    ans1.append(ans)
    for i in range(n - 1):
        x, y = list(map(int, input().split()))
        p, q = ans1[-1][0], ans1[-1][1]
        if p % x == 0:
            p1 = p // x
        else:
            p1 = p // x + 1
        if q % y == 0:
            q1 = q // y
        else:
            q1 = q // y + 1
        pq = max(p1, q1)
        r = [x * pq, y * pq]
        ans1.append(r)

    print((sum(ans1[-1])))
