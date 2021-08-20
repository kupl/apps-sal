n = int(input())
a = list(map(int, input().split()))
cnt = [0] * 1000005
for x in a:
    if cnt[x] != 0:
        cnt[x] = 2
    else:
        for i in range(x, 1000005, x):
            cnt[i] += 1
ans = 0
for x in a:
    if cnt[x] == 1:
        ans += 1
print(ans)
