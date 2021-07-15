from math import ceil
n, m = map(int, input().split())
ans = 0
for i in range(1, m + 1):
    for j in range(1, m + 1):
        if (i ** 2 + j ** 2) % m == 0:
            ch1, ch2 = ceil((n - i + 1) / m), ceil((n - j + 1) / m)
            ans += ch1 * ch2
print(ans)
