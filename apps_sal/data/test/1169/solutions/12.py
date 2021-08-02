(n, m) = map(int, input().split())

if (n + 1) // 2 <= m:
    print(0, end=' ')
else:
    print(n - m * 2, end=' ')

k = 0
while k < n:
    if (k * (k - 1)) // 2 < m:
        k += 1
        continue
    else:
        break

print(n - k)
