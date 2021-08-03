n = int(input())
a = [*map(int, input().split())]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans += a[i] * a[j]
print(ans)
