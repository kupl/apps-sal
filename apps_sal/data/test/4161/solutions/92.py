

import math
rst = 0
K = int(input())
for i in range(1, K + 1):
    for j in range(1, K + 1):
        tmp = math.gcd(i, j)
        for k in range(1, K + 1):
            rst += math.gcd(k, tmp)
print(rst)
