import math
n = int(input())
a = [*map(int, input().split())]
ans = 0
for i in a:
    ans = math.gcd(ans, i)
print(ans)
