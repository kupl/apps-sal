n, s, ans = int(input()), input(), 0
for i in range(len(s)):
    if i > 2 and not i % n and s[i - 1] == s[i - 2] == s[i - 3]:
        ans += 1
print(ans)
