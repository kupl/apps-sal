# cook your dish here
import math
n = int(input())
l = list(map(int, input().split()))
s = sum(l)
z = math.trunc(math.sqrt(1 + 8 * s))
z = (-1 + z) // 2
if z == n:
    print("YES")
else:
    print("NO")
