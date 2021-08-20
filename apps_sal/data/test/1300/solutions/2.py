(n, c) = list(map(int, input().split()))
cnt = [0] * 500005
ans = 0
for v in map(int, input().split()):
    if v == c:
        cnt[c] = cnt[c] + 1
    else:
        if cnt[v] < cnt[c]:
            cnt[v] = cnt[c]
        cnt[v] += 1
    ans = max(ans, cnt[v] - cnt[c])
print(ans + cnt[c])
