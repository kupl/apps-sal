(n, m) = map(int, input().split())
x = dict()
for i in range(n):
    (a, b) = map(int, input().split())
    if a * b not in x:
        x[a * b] = 1
    else:
        x[a * b] += 1
cnt = 0
for i in range(m):
    (a, b) = map(int, input().split())
    if a * b in x and x[a * b] != 0:
        x[a * b] -= 1
        cnt += 1
print(cnt)
