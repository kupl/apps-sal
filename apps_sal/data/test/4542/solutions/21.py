s = input()
c = s[0]
ans = 0
for i in range(1, len(s)):
    if c != s[i]:
        ans += 1
    c = s[i]
print(ans)
