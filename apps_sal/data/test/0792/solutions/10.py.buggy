n, d = list(map(int, input().split()))
l = list(map(int, input().split()))
mus = [0] * n
mus[0] = l[0]
cnt = 0
ans = 0
for i in range(1, n):
    mus[i] = mus[i - 1] + l[i]
suf = [0] * n
suf[-1] = mus[-1]
for i in range(n - 2, -1, -1):
    suf[i] = max(mus[i], suf[i + 1])
for i in range(n):
    if l[i] == 0 and mus[i] + cnt < 0:
        if (d - suf[i] - cnt < 0 or d - suf[i] < abs(mus[i])):
            print(-1)
            return
        else:
            cnt += (d - suf[i] - cnt)
            ans += 1
if suf[0] > d:
    print(-1)
    return
print(ans)
