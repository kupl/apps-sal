s = input()
t = input()
ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans = ans + 1
print(ans)

