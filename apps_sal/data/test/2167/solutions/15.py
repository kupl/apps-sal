import math

n = int(input())
ans = 0

for x in input().split():
    ans += int(x)

if n == 1:
    ans = 1
else:
    if ans == int(ans/n)*n:
        ans = n
    else:
        ans = n-1

print(ans)

