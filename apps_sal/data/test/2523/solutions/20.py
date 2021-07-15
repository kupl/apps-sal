s = input()
l = len(s)
ans = l
for i in range(l - 1):
    if s[i] != s[i + 1]:
        ans = min(ans, max(i + 1, l - i - 1))
print(ans)
