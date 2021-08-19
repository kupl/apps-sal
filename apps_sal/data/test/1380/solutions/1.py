(n, k) = list(map(int, input().split()))
a = [int(x) for x in input().split()]
a2 = [a[i] - k * i for i in range(n)]
bs = set(a2)
(bestKey, maxCount) = (1, 0)
for key in bs:
    if key <= 0:
        continue
    count = a2.count(key)
    if count > maxCount:
        bestKey = key
        maxCount = count
b = bestKey
print(n - maxCount)
for i in range(n):
    if a[i] > i * k + b:
        print('-', i + 1, a[i] - (i * k + b))
    elif a[i] < i * k + b:
        print('+', i + 1, i * k + b - a[i])
