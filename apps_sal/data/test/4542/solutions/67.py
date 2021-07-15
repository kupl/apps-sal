s = list(input())
ans = 0
t = s[0]
for i in range(1,len(s)):
    if s[i] != t:
        t = s[i]
        ans += 1
print(ans)
