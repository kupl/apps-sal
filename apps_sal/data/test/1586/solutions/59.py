import sys

N = int(input())

if N % 2 == 0:
    k = N // 2
    tmp = 5
    ans = 0
    while k >= tmp:
        ans += k // tmp
        tmp *= 5
else:
    ans = 0
print(ans)
