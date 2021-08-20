(x, y) = list(map(float, input().split(' ')))
(x1, y1) = list(map(float, input().split(' ')))
n = int(input())
r = 0
for i in range(n):
    (a, b, c) = list(map(float, input().split(' ')))
    q1 = a * x + b * y + c
    q2 = a * x1 + b * y1 + c
    if q1 > 0 and q2 < 0 or (q1 < 0 and q2 > 0):
        r += 1
print(r)
