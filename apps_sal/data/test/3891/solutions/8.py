(n, m) = list(map(int, input().split()))
s = [None] * n
for i in range(n):
    s[i] = input()
LIST = []
for i in range(n):
    for j in range(m):
        if s[i][j] == 'B':
            LIST.append((i + 1, j + 1))
x = min(LIST)[0] + max(LIST)[0]
y = min(LIST, key=lambda x: x[1])[1] + max(LIST, key=lambda x: x[1])[1]
print(x // 2, y // 2)
