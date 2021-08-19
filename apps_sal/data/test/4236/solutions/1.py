(n, m) = map(int, input().split())
ar = [0] * m
for i in range(n):
    (a, b) = map(int, input().split())
    for e in range(a - 1, b):
        ar[e] = 1
ans = []
for i in range(m):
    if ar[i] == 0:
        ans.append(i + 1)
print(len(ans))
print(*ans)
