n, m = map(int, input().split())
x = [False] * 101

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b):
        x[i] = True

for i in range(m):
    if not x[i]:
        print('NO')
        return
print('YES')
