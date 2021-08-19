from decimal import Decimal
import sys
import math


def input():
    return sys.stdin.readline().rstrip()


M = 10 ** 6 + 5
N = int(input())
A = list(map(int, input().split()))
count = [0] * M
for a in A:
    if count[a] != 0:
        count[a] = 2
        continue
    for i in range(1, M):
        if i * a >= M:
            break
        count[a * i] += 1
ans = 0
for a in A:
    if count[a] == 1:
        ans += 1
print(ans)
