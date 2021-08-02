import math
import collections
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

s = input()

cnt = 0
for i in range(len(s) // 2):
    if s[i] != s[-1 - i]:
        cnt += 1
print(cnt)
