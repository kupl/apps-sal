from math import sqrt
(x, y) = map(int, input().split())
n = int(input())
mas = []
for i in range(n):
    (a, b, c) = map(int, input().split())
    mas.append(sqrt((a - x) * (a - x) + (b - y) * (b - y)) / c)
mas.sort()
print(mas[0])
