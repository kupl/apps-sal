d = [0] * 1000
(n, m) = list(map(int, input().split()))
for i in range(m):
    (u, v) = list(map(int, input().split()))
    d[u - 1] = 1
    d[v - 1] = 1
for i in range(n):
    if d[i] == 0:
        c = i
        break
print(n - 1)
for i in range(n):
    if i == c:
        continue
    print(c + 1, i + 1)
