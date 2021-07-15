keke = dict()
ans = 0
s = input().strip()
for i in range(0, len(s)):
    if not s in keke:
        keke[s] = 1
        ans+= 1
    s = s[-1] + s[:-1]
print(ans)
