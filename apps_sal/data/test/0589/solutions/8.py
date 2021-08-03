s = input()

z = set()
us = 0

ans = 1
if s[0] == '?' or (s[0] >= 'A' and s[0] <= 'J'):
    ans = 9
    z.add(s[0])
    if s[0] >= 'A' and s[0] <= 'J':
        us += 1

i = -1
for x in s:
    i += 1
    if i == 0:
        continue
    if x == '?':
        ans *= 10
    if x >= 'A' and x <= 'J':
        if x not in z:
            ans *= (10 - us)
            z.add(x)
            us += 1

print(ans)
