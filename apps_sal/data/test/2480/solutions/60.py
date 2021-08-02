n, k = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
for i in range(n):
    a[i + 1] += a[i]
cnt = {}
ans = 0
for i in range(n + 1):
    left = i - k
    if left >= 0:
        ldiff = (a[left] - left) % k
        cnt[ldiff] -= 1
    diff = (a[i] - i) % k
    if diff not in cnt:
        cnt[diff] = 0
    ans += cnt[diff]
    cnt[diff] += 1
print(ans)
