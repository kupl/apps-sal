import math
(a, b) = input().split()
n = int(a + b)
print('Yes') if math.sqrt(n) % 1 == 0 else print('No')
