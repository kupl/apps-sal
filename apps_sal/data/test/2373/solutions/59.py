input()
cnt, ans = 0, 0
for i, p in enumerate(map(int, input().split()), start=1):
    if i == p:
        cnt += 1
    else:
        ans += (cnt + 1) // 2
        cnt = 0
else:
    ans += (cnt + 1) // 2
print(ans)
