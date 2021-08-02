import math
n, k = list(map(int, input().split()))
a = int(math.log(n, k)) + 1
print(a)
