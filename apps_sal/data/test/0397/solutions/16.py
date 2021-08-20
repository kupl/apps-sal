import math
(n, k) = [int(x) for x in input().split(' ')]
ans = (2 * n + 3 - int(math.sqrt(8 * n + 8 * k + 9))) // 2
print(ans)
