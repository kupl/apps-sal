import math
n = int(input())
for i in range(n):
    (l, r) = [*map(int, input().split())]
    l -= 1
    war1 = math.ceil(l / 2)
    if l % 2 == 1:
        war1 = -1 * war1
    war2 = math.ceil(r / 2)
    if r % 2 == 1:
        war2 = -1 * war2
    print(war2 - war1)
