s = input()
ans = 0
for i in range(len(s), 0, -1):
    for j in range(i - 1, len(s)):
        if s[j - i + 1:j + 1] != s[j - i + 1:j + 1][::-1]:
            ans = max(ans, i)
print(ans)

