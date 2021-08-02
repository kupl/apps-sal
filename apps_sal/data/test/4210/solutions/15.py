from collections import Counter
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

D = [Counter() for i in range(11)]
for a in A:
    for j in range(1, 11):
        D[j][a * (10**j) % k] += 1

ANS = 0
for a in A:
    L = len(str(a))
    x = -a % k

    if a * (10**L) % k == x:
        ANS -= 1

    ANS += D[L][x]

print(ANS)
