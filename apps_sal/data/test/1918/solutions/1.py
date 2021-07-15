read = lambda: list(map(int, input().split()))
n = int(input())
p = list(read())
a = [{'B': 1, 'A': 0}[i] for i in input()]
cur = sum(p[i] for i in range(n) if a[i])
ans = cur
b = a[:]
for i in range(n):
    b[i] = int(not a[i])
    if b[i]: cur += p[i]
    else: cur -= p[i]
    ans = max(ans, cur)
cur = sum(p[i] for i in range(n) if a[i])
b = a[:]
for i in range(n - 1, -1, -1):
    b[i] = int(not a[i])
    if b[i]: cur += p[i]
    else: cur -= p[i]
    ans = max(ans, cur)
print(ans)

