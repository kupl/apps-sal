import math


def get(k):
    n = (-1 + math.sqrt(1 + 8 * k)) // 2
    (z, last) = (True, 1)
    length = 0
    while z:
        length = length + len(str(last))
        if k > length:
            k -= length
            last += 1
        else:
            z = False
    last = 1
    while k > 0:
        k -= len(str(last))
        last += 1
    if k == 0:
        print(str(last - 1)[-1])
    if k < 0:
        print(str(last - 1)[len(str(last - 1)) + k - 1])


t = int(input())
for _ in range(t):
    k = int(input())
    get(k)
