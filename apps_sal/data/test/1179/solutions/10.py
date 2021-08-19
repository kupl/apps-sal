import math
(n, k) = [int(x) for x in input().split()]
ID = [int(x) for x in input().split()]
m = math.floor(((1 + 8 * (k - 1)) ** 0.5 - 1) / 2)
print(ID[k - 1 - m * (m + 1) // 2])
