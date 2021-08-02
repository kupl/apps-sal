import math
n = int(input())
ans = 1

p = [7, 11, 13, 17, 19, 23, 29]

for j in p:
    if j > n:
        break
    ans *= j

ans *= 2**math.floor(math.log(n, 2)) * 3**math.floor(math.log(n, 3)) * 5**math.floor(math.log(n, 5))

print((ans + 1))
