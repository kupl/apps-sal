import sys
(n, K) = list(map(int, sys.stdin.readline().split()))
a = sorted(list(map(int, sys.stdin.readline().split())))
eaten = set()
for i in range(1, n):
    (x, y) = (a[i - 1], a[i])
    if y > x and y <= x + K:
        eaten.add(x)
print(n - sum((x in eaten for x in a)))
