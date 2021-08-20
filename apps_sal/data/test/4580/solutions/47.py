n = int(input())
a = list(map(int, input().split()))
cnt = [0] * 9
for i in a:
    x = min(i // 400, 8)
    if x >= 8:
        cnt[8] += 1
    else:
        cnt[x] = 1
if sum(cnt[:8]) == 0:
    l = 1
    r = cnt[8]
else:
    l = sum(cnt[:8])
    r = l + cnt[8]
print(l, r)
