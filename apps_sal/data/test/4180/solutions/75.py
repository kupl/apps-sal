import math
n = int(input())
x = math.ceil(n / 1000)
ans = (x * 1000) - n
print(ans)
