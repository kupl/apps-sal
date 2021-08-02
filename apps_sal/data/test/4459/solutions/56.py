n = int(input())
a = list(map(int, input().split()))
cnt = dict()

for ai in a:
    if ai not in list(cnt.keys()):
        cnt[ai] = 1
    else:
        cnt[ai] += 1

ans = 0
for k in list(cnt.keys()):
    if cnt[k] > k:
        ans += cnt[k] - k
    elif cnt[k] < k:
        ans += cnt[k]
print(ans)
