from collections import Counter
import sys
import os
import io
input = sys.stdin.readline
T = int(input())
ans = [0] * T
for t in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    p = 0
    ans[t] = 'Second'
    if n % 2 == 0:
        C = Counter(A)
        for v in C.values():
            if v % 2 == 1:
                ans[t] = 'First'
                break
print(*ans, sep='\n')
