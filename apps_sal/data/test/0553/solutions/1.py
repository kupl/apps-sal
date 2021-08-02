n = int(input())
codes = []
for i in range(n):
    codes.append(input())


def change(a, b, k):
    x = 0
    for i in range(6):
        if a[i] != b[i]:
            x += 1
        if x == k:
            return 3
    if x % 2 == 0:
        return x // 2 - 1
    return x // 2


if n == 1:
    print(6)
    return

k = 2
for i in range(n):
    for j in range(i + 1, n):
        if change(codes[i], codes[j], 2 * k + 1) < k:
            k = change(codes[i], codes[j], 2 * k + 1)
        if k == 0:
            break
print(k)
