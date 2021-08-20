(n, k) = list(map(int, input().split()))
ai = list(map(int, input().split()))
ans = 0
for i in range(n):
    if ai[i] > k:
        break
    ans += 1
for i in range(n - 1, -1, -1):
    if ai[i] > k:
        break
    ans += 1
print(min(n, ans))
