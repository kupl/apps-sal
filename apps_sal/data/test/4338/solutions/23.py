import math
(n, x, y) = list(map(int, input().split()))
a = [int(x) for x in input().split()]
if x > y:
    print(n)
else:
    counter = 0
    for i in a:
        if x >= i:
            counter += 1
    print(math.ceil(counter / 2))
