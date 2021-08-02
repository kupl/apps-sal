import math
a, b, c, x, y = map(int, input().split(' '))
ans = float('inf')
c = c * 2
for i in range(max(x, y) + 1):
    if i > x:
        price = b * (y - i) + c * i
    elif i > y:
        price = a * (x - i) + c * i
    else:
        price = a * (x - i) + b * (y - i) + c * i

    if ans > price:
        ans = price
print(ans)
