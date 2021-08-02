n, k = map(int, input().split())
H = []
for i in range(n):
    H.append(int(input()))
H.sort()
ans = 10**9 + 2
for i in range(n - k + 1):
    ans = min(ans, H[i + k - 1] - H[i])
print(ans)
