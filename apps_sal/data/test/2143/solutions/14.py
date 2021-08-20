n = int(input())
a = list(map(int, input().split()))
sm = []
for i in range(n):
    for j in range(i + 1, n):
        sm.append(a[i] + a[j])
cnt = dict()
ans = 0
for i in sm:
    if i not in cnt.keys():
        cnt[i] = 1
    else:
        cnt[i] += 1
for i in sm:
    ans = max(cnt[i], ans)
print(ans)
