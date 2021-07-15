def check(x):
    ans = 0
    for i in range(101):
        ans += cnt[i] // x
    return ans >= n


n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * 101
for elem in a:
    cnt[elem] += 1
l = 0
r = m + 1
while r - l > 1:
    mid = (r + l) // 2
    if not check(mid):
        r = mid
    else:
        l = mid
print(l)
