n = int(input())
ans = []
for i in range(0, 64):
    y = 2 ** i
    deter = (y - 3) ** 2 + (4 * 2 * n)
    if deter >= 0:
        sqrt = int(pow(deter, .5))
        while(sqrt * sqrt < deter):
            sqrt += 1
        while(sqrt * sqrt > deter):
            sqrt -= 1
        if(sqrt * sqrt == deter):
            ev1 = 3 - y + sqrt
            if(ev1 % 2 == 0):
                ev1 /= 2
                if(ev1 > 0 and ev1 % 2 == 1):
                    for j in range(0, i):
                        ev1 *= 2
                    ans.append(ev1 / 2)

            ev1 = 3 - y - sqrt
            if(ev1 % 2 == 0):
                ev1 /= 2
                if(ev1 > 0 and ev1 % 2 == 1):
                    for j in range(0, i):
                        ev1 *= 2
                    ans.append(ev1 / 2)
for i in sorted(ans):
    print(int(i))
if not len(ans):
    print(-1)
