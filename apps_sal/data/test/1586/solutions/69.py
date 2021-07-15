import sys


N = int(input())


if N % 2 != 0:
    print((0))
    return

N //= 10
cnt = 0
while N > 0:
    cnt += N
    N //= 5

print(cnt)

