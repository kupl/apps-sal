import math
n, k = map(int, input().split())
x = int(math.log(n)//math.log(k)) + 1
print(x)
