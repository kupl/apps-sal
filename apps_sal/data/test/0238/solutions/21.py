n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))

values = list()

for j in range(n):
    result = a[j]
    sum1 = 0
    for i in range(m):
        if j - i >= 0:
            sum1 = sum1 + a[j - i]
            if sum1 > result:
                result = sum1
        else:
            continue
    if j - m >= 0:
        result = max(result, sum1 + values[j - m])
    values.append(max(0, result - k))
print((max(values)))
