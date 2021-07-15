n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

i = 1
while i * (i + 1) < 2 * k:
    i += 1
i -= 1
print(a[k - 1 - i * (i + 1) // 2])

