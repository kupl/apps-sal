from sys import stdin, stdout
from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial
n = int(stdin.readline())
values = list(map(int, stdin.readline().split()))
ans = float('inf')
for i in range(n):
    cnt = 0
    for j in range(n):
        cnt += values[j] * (abs(i - j) + j + i + (i + j + abs(j - i)))
    ans = min(ans, cnt)
stdout.write(str(ans))
