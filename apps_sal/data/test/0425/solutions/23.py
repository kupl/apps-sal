import math
x, y = list(map(int, input().split()))

i = 1
n = x - (i * y)
while n >= 1:
    a = 0
    for j in str(bin(n))[2:]:
        a += int(j)
        a *= 2
    a //= 2
    if str(bin(n))[2:].count('1') <= i and i <= a:
        print(i)
        break
    i += 1
    n = x - (i * y)
else:
    print(-1)
