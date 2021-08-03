import math

N = int(input())

if N % 2 == 1:
    print(0)
    return

ans = 0
i = 1
while 1:
    a = 2 * 5**i
    if N // a == 0:
        break
    ans += (N // a)
    i += 1
print(ans)
