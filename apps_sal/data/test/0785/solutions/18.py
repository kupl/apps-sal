import math
x = []
count = 0
(n, a, b) = list(map(int, input().split()))
if a > b:
    count = 1
if a * b >= n * 6:
    print(a * b)
    print(a, b)
elif max(a, b) <= n and min(a, b) <= 6:
    print(n * 6)
    if count == 1:
        print(max(n, 6), min(n, 6))
    else:
        print(min(n, 6), max(n, 6))
else:
    for i in range(min(a, b), min(math.ceil(n * 6 / min(a, b)), int((6 * n) ** 0.5)) + 1):
        if math.ceil(n * 6 / i) >= max(a, b):
            x.append([math.ceil(n * 6 / i) * i, i])
    x.sort()
    print(x[0][0])
    if count == 1:
        print(max(x[0][1], x[0][0] // x[0][1]), min(x[0][1], x[0][0] // x[0][1]))
    else:
        print(min(x[0][1], x[0][0] // x[0][1]), max(x[0][1], x[0][0] // x[0][1]))
