n = int(input())
a = list(map(int, input().split(' ')))
d = [0] * n
for item in a:
    d[item - 1] += 1
result = 0
for i in range(n - 1):
    dm1 = d[i] - 1
    if dm1 < 0:
        continue
    d[i + 1] += dm1
    result += dm1
result += d[n - 1] * (d[n - 1] - 1) // 2
print(result)
