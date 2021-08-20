n = int(input())
arr = [int(x) for x in input().split()]
cnt = [0] * (10 ** 5 + 1)
for a in arr:
    cnt[a] += 1
    cnt[a + 1] += 1
    if a > 0:
        cnt[a - 1] += 1
print(max(cnt))
