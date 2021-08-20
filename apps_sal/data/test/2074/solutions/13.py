import sys
(n, m) = list(map(int, sys.stdin.readline().split()))
t = -1
for i in range(n):
    a = [1] * m
    a = list(map(int, sys.stdin.readline().split()))
    k = min(a)
    t = max(k, t)
print(t)
