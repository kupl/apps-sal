import math
m, R = map(int, input().split())
cord = math.sqrt(2 * (R**2))
li = 0
unit = int(2 * R)
x = (m) * (m / 2)
for i in range(m):
    li += 2 * R * m
    li += (cord * (m - 1))
    if(i == 0 or i == m - 1):
        if(m == 1):
            continue
        li += cord * (m - 2)
    else:
        if(m == 1):
            continue
        li += cord * (m - 3)
    left = (i - 1) - 1
    if(left < -1):
        left = -1
    li += (left + 1) * (left / 2) * unit
    r = (m - 1) - (i) - 2
    if(r < -1):
        r = -1
    li = li + (r + 1) * (r / 2) * unit
li /= (m**2)
print(li)
