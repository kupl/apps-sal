import math


def check(x):
    limit = math.ceil(math.sqrt(x))

    for i in range(3, limit + 1, 2):
        if x % i == 0:
            return i
    return x


p, y = list(map(int, input().split()))

ans = -1

if y % 2 == 0:
    y -= 1

for x in range(y, p, -2):
    q = check(x)
    if q > p:
        ans = x
        break
print(ans)
