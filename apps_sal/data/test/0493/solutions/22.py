n = int(input())
s = input().split('L')
ans = 0
if 'R' not in s[0]:
    if len(s) != 1:
        s = s[1:]
if 'R' in s[-1]:
    s[-1] = s[-1][:s[-1].index('R')]
for sub in s:
    if 'R' not in sub:
        ans += len(sub)
    else:
        idx = sub.index('R')
        ans += idx
        ans += (len(sub) - idx - 1) % 2
print(ans)
