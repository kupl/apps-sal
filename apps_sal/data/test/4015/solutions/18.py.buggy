import sys
n, m = list(map(int, input().split()))

if m / n != m // n:
    print(-1)
    return

x = m // n
ANS = 0

while x % 2 == 0:
    x = x // 2
    ANS += 1

while x % 3 == 0:
    x = x // 3
    ANS += 1

if x == 1:
    print(ANS)
else:
    print(-1)
