(n, m) = map(int, input().split())
height = [0] + list(map(int, input().split()))
mawari = [0] * (n + 1)
ans = 0
for _ in range(m):
    (a, b) = map(int, input().split())
    mawari[a] = max(mawari[a], height[b])
    mawari[b] = max(mawari[b], height[a])
for i in range(1, n + 1):
    if height[i] > mawari[i]:
        ans += 1
print(ans)
