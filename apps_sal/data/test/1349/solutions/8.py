import sys
import math
t = int(input())
for i in range(t):
    (n, k) = list(map(int, input().split()))
    x = list(map(int, input().split()))
    h = [0 for i in range(n)]
    tm = 0
    while 1:
        for j in x:
            if j - tm - 1 >= 0:
                h[j - tm - 1] = 1
            if j + tm - 1 < n:
                h[j - 1 + tm] = 1
        if sum(h) == n:
            print(tm + 1)
            break
        tm += 1
