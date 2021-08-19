n = int(input())
d = list(map(int, input().split()))
ans = 0
for i in range(0, n):
    for j in range(i + 1, n):
        ans += d[i] * d[j]
print(ans)
