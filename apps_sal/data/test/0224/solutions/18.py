s = input()

ans = 1
cnt = 0
for c in s:
    cnt += 1
    if c in ['A', 'I', 'U', 'E', 'O', 'Y']:
        ans = max(cnt, ans)
        cnt = 0

ans = max(ans, cnt + 1)
print(ans)
