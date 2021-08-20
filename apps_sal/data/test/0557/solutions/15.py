(n, m) = list(map(int, input().split()))
c = [False for i in range(m + 1)]
for i in range(n):
    (x, y) = list(map(int, input().split()))
    for j in range(x + 1, y + 1):
        c[j] = True
print('YES' if all(c[1:]) else 'NO')
