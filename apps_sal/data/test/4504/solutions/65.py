s = input()
ans = 0
for _ in range(1,len(s)):
    s = s[:-1]
    if len(s)%2==0:
        if s[:len(s)//2]==s[len(s)//2:]:
            ans = max(ans,len(s))
    else:
        continue
print(ans)
