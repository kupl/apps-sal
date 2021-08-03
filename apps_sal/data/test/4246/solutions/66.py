s = str(input())
t = str(input())
ans = 0
for i in range(len(s)):
    if s[i] == t[i]:
        ans += 1
print(ans)
