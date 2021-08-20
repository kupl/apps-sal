import sys
n = int(input())
i = 0
ANS = []
while n > 0:
    if n == 3:
        ANS = ANS + [2 ** i, 2 ** i, 3 * 2 ** i]
        break
    x = (n + 1) // 2
    ANS = ANS + [2 ** i] * x
    n = n - x
    i += 1
for a in ANS:
    print(a, end=' ')
