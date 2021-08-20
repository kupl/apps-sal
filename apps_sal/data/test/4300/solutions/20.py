n = int(input())
D = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        ans += D[i] * D[j]
print(ans)
