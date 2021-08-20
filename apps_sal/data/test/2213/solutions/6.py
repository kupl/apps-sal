(n, m, k) = map(int, input().split())
print(m * (m - 1) // 2)
for i in range(m - 1):
    for j in range(1, m - i):
        print('{} {}'.format(*((j + 1, j) if k else (j, j + 1))))
