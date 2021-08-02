n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    z = 0
    for j in range(i + 1):
        z += a[j]
    for j in range(i, n):
        z += b[j]
    ans = max(ans, z)
print(ans)
