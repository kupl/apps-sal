from math import atan2
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort(key=lambda x: atan2(x[1], x[0]))
ans = 0
for lp in range(n):
    for rg in range(n):
        lf = lp
        x, y = l[lf]
        lf += 1
        if lf == n:
            lf = 0
        while lf != rg:
            x += l[lf][0]
            y += l[lf][1]
            lf += 1
            if lf == n:
                lf = 0
        ans = max(ans, (x ** 2 + y ** 2) ** .5)
print(ans)

