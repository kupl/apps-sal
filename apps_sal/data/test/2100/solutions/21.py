"""input
5
0 1
1 0
0 1
1 1
0 1
"""
n = int(input())
(x, y) = ([], [])
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    x.append(a)
    y.append(b)
print(min(x.count(0), x.count(1)) + min(y.count(0), y.count(1)))
