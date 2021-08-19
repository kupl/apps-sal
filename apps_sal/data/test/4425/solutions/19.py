(n, k) = map(int, input().split())
a = []
for i in range(1, n + 1):
    x = i
    b = 0
    while x < k:
        x = x * 2
        b += 1
    a.append(float(1 / n) * 0.5 ** b)
print(sum(a))
