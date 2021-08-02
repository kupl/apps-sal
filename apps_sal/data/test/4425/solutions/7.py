import math
import sys
input = sys.stdin.readline
n, k = list(map(int, input().split()))
#a = list(map(int,input().split()))

par = 0

for i in range(1, n + 1):
    tmp = i
    cnt = 0
    while True:
        if tmp >= k:
            break
        tmp *= 2
        cnt += 1
    if cnt == 0: par += 1 / n
    else: par += 1 / (2**cnt * n)

print(f'{par:.12f}')
