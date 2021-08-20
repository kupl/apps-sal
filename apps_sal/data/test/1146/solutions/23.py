(n, m) = list(map(int, input().split()))
b = [None] + [False for i in range(m)]
for i in range(n):
    (a, *q) = list(map(int, input().split()))
    for e in q:
        b[e] = True
T = True
for i in b[1:]:
    T = T and i
print('YES' if T else 'NO')
