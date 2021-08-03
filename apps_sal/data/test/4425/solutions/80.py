n, k = map(int, input().split())

sum1 = 0
for i in range(1, n + 1):
    p = 0
    while True:
        if (2**p) * i >= k:
            break
        p += 1
    sum1 += 1 / (n * 2**p)
print(sum1)
