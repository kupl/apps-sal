(m, n) = list(map(int, input().split()))
a = [[0] * m for i in range(n)]
for i in range(n):
    h = input()
    for j in range(m):
        a[i][j] = h[j]
s = list(zip(*a))
b = [[0] * 2 * n for i in range(2 * m)]
for i in range(2 * m):
    for j in range(2 * n):
        b[i][j] = s[i // 2][j // 2]
for i in b:
    print(''.join(map(str, i)))
