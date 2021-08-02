import math
3


n = int(input())
x = math.floor(math.sqrt(n * 2))

while n <= x * (x + 1) // 2:
    x -= 1

ans = n - x * (x + 1) // 2
print(ans)
