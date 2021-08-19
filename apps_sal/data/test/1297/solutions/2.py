s = input()
p = s[0]
cnt = 1
ans = 0
for i in range(1, len(s)):
    if s[i] == p:
        cnt += 1
    else:
        if cnt % 2 == 0:
            ans += 1
        p = s[i]
        cnt = 1
if cnt % 2 == 0:
    ans += 1
print(ans)
