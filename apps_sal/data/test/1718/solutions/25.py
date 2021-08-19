import math
(n, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
print(math.ceil((n - 1) / (k - 1)))
