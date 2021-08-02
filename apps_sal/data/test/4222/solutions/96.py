import numpy as np
n, k = list(map(int, input().split()))
l = [0 for i in range(n)]
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in a:
        l[j - 1] = 1

print((l.count(0)))
