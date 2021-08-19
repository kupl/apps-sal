(a, b, c, d) = map(int, input().split())
result_1 = []
result_2 = []
if a <= b and c <= d:
    x = [a, b]
    y = [c, d]
    r1 = x[0] * y[0]
    r2 = x[0] * y[1]
    result_1.append(r1)
    result_1.append(r2)
    r3 = x[1] * y[0]
    r4 = x[1] * y[1]
    result_2.append(r3)
    result_2.append(r4)
    x = max(result_1)
    y = max(result_2)
    result = max(x, y)
print(result)
