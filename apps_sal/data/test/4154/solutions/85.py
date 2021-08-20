(n, m) = list(map(int, input().split()))
count = [0] * (n + 1)
for i in range(m):
    (l, r) = list(map(int, input().split()))
    l -= 1
    count[l] += 1
    count[r] -= 1
for i in range(n):
    count[i + 1] += count[i]
ans = 0
for i in range(n):
    if count[i] == m:
        ans += 1
print(ans)
