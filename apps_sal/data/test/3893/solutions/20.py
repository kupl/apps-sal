(x1, y1) = list(map(int, input().split()))
(x2, y2) = list(map(int, input().split()))
n = int(input())
cost = 0
for i in range(n):
    (a, b, c) = list(map(int, input().split()))
    d1 = a * x1 + b * y1 + c
    d2 = a * x2 + b * y2 + c
    if d1 * d2 < 0:
        cost += 1
print(cost)
