s = input()
ans = 0
n = len(s)
for i in range((n + 1) // 2):
    if s[i] != s[-i - 1]:
        ans += 1
print(ans)
