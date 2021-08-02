import sys
n = int(input())
ans = 0
while n > 0:
    ans += n
    n -= 2
print(ans)
