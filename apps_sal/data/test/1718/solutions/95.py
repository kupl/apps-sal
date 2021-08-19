import math
(n, k) = list(map(int, input().strip().split(' ')))
window = k - 1
res = math.ceil((n - 1) / window)
print(res)
