a = list(map(int, input().split()))
cnt = [0] * 1000
for i in a:
    cnt[i] += 1
s = sum(a)
res = s
for i in range(1000):
    cnt[i] = min(cnt[i], 3)
    if 2 <= cnt[i]:
        res = min(res, s - cnt[i] * i)
print(res)
