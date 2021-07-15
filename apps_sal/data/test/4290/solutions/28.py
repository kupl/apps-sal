n,m = map(int,input().split())
import math

a = (n * (n - 1)) / 2

b = (m * (m - 1)) / 2

print(math.floor(a + b))
