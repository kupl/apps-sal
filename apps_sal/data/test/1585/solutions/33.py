import math
x, y = map(int, input().split())
ans = 0

#ans = int(math.log2(y/x))

while y >= x:
    x = x * 2
    ans += 1

print(ans)
