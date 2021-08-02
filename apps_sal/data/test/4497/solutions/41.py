import math

n = int(input())
ans, i = 0, 1
while ans <= n:
    ans = 2**i
    i += 1

print(ans // 2)
