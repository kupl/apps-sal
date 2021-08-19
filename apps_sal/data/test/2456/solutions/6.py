from sys import stdin, stdout
import math
t = int(stdin.readline())
for _ in range(t):
    (n, r) = list(map(int, stdin.readline().split()))
    cnt = 0
    if r < n:
        print(r * (r + 1) // 2)
    else:
        print(n * (n - 1) // 2 + 1)
