n = int(input())
maxn = 10 ** 6 + 2
cnt = [0] * maxn
for x in map(int, input().split()):
    cnt[x] += 1
ansv = []
for i in range(maxn - 2, 1, -1):
    ansv += [i] * (cnt[i] + (cnt[i + 1] & 1) >> 1)
    if cnt[i] > 0:
        cnt[i] += cnt[i + 1] & 1
ans = 0
for i in range(1, len(ansv), 2):
    ans += ansv[i] * ansv[i - 1]
print(ans)
