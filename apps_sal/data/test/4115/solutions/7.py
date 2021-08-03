s = input()
slen = len(s)
ans = 0
for i in range(slen // 2):
    if s[i] != s[-(i + 1)]:
        ans += 1
print(ans)
