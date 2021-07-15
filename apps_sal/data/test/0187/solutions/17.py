n = int(input())
a = [int(input()) for _ in range(n)]

cnt = {}
for ai in a:
    if ai in cnt:
        cnt[ai] += 1
    else:
        cnt[ai] = 1
ans = []
for k, v in list(cnt.items()):
    if v * 2 == n:
        ans.append(k)
if len(cnt) != 2:
    ans = []
if len(ans) == 2:
    print("YES")
    print(' '.join(map(str, ans)))
else:
    print("NO")

