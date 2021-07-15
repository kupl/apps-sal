s = input() * 2
ans = cur = 1
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 1
ans = min(ans, len(s) // 2)
print(ans)
