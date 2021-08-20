def R():
    return list(map(int, input().split()))


(n, a) = R()
b = list(R())
sum = 0
for i in range(n):
    sum += b[i]
for i in range(n):
    print(b[i] - min(b[i], a - n + 1) + max(1, a - sum + b[i]) - 1, end=' ')
