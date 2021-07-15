n, k = list(map(int, input().split()))
cnt = [0] * k
for i in range(n):
    x = int(input())
    cnt[x - 1] += 1
ans = 0
p = 0
for i in range(k):
    p += cnt[i] // 2
    ans += cnt[i] // 2 * 2
ans += (n + 1) // 2 - p
print(ans)

