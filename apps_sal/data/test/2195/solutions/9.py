from math import inf
t = int(input())
for q in range(t):
    x, y = [int(i) for i in input().split()]
    a, b = [int(i) for i in input().split()]
    print(min(a * (x + y), a * abs(x - y) + b * min(x, y)))

