n = int(input())
num = list(map(int, input().split()))

cnt = {}
cursum = 0
ans = 0

for i in range(n):
    ans += num[i] * i - cursum

    if (num[i] - 1) in cnt:
        ans -= cnt[num[i] - 1]
    if (num[i] + 1) in cnt:
        ans += cnt[num[i] + 1]

    cursum += num[i]
    if num[i] not in cnt:
        cnt[num[i]] = 0
    cnt[num[i]] += 1

print(ans)

