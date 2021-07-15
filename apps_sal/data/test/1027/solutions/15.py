a = list(map(int, input().split()))

result = 0

for i in range(14):
    b = a[:]
    b[i] = 0

    for j in range(i + 1, i + 15):
        b[j % 14] += a[i] // 14

    for j in range(i + 1, i + 1 + a[i] % 14):
        b[j % 14] += 1

    result = max(result, sum([x for x in b if x % 2 == 0]))

print(result)
