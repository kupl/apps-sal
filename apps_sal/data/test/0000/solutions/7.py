s = input()

f1 = False
f2 = False
l1 = -1
for l in range(len(s)):
    if f1 == False and s[l] == '[':
        f1 = True
    elif f1 == True and s[l] == ':':
        f2 = True
        l1 = l
        break
g1 = False
g2 = False
r1 = -1
for r in range(len(s) - 1, -1, -1):
    if g1 == False and s[r] == ']':
        g1 = True
    elif g1 == True and s[r] == ':':
        g2 = True
        r1 = r
        break
if (l1 == -1 or r1 == -1) or (r1 <= l1):
    print(-1)

else:
    ans = 4
    for i in range(l1 + 1, r1):
        if s[i] == '|':
            ans += 1
    print(ans)
