import math

l, r = map(int, input().split())

if l == r:
    print("0")
else:
    msb = int(math.log2(r))
    for i in range(msb, -1, -1):
        if (l & (1 << i)) != (r & (1 << i)):
            break

    print(2 * (1 << i) - 1)
