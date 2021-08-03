n, m = map(int, input().split())

a = [[0 for _ in range(m)] for _ in range(n)]
b = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
    a[i] = list(map(int, input().split()))


for i in range(n):
    b[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        a[i][j], b[i][j] = min(a[i][j], b[i][j]), max(a[i][j], b[i][j])

# print('a:')
# print(a)

# print('b:')
# print(b)

works = True

for i in range(n):
    for j in range(m - 1):
        if a[i][j + 1] <= a[i][j]:
            works = False

        if b[i][j + 1] <= b[i][j]:
            works = False

for j in range(m):
    for i in range(n - 1):
        if a[i + 1][j] <= a[i][j]:
            works = False

        if b[i + 1][j] <= b[i][j]:
            works = False

if works:
    print('Possible')
else:
    print('Impossible')
