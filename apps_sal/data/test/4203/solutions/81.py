s = list(input())
ans = 'AC'
if s[0] != 'A':
    ans = 'WA'
c_idx = None
for i, v in enumerate(list(s)):
    if i >= 2 and i <= len(s)-2:
        if v == 'C':
            if c_idx is None:
                c_idx = i
            else:
                ans = 'WA'
if c_idx is None:
    ans = 'WA'
else:
    s[0] = 'a'
    s[c_idx] = 'c'
    if [ i.lower() for i in s ] != s:
        ans = 'WA'
print(ans)
