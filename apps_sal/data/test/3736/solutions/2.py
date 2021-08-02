s = input()
z = ['A', 'H', 'M', 'T', 'U', 'V', 'W', 'O', 'I', 'X', 'Y']

f1 = True
if (s[::-1] == s):
    f1 = True
else:
    f1 = False


sa = set()
v = True
for i in range(0, len(s)):
    sa.add(s[i])

sals = list(sa)
for i in range(0, len(sals)):
    if (sals[i] in z):
        v = True
    else:
        v = False
        break

if (f1 == True and v == True):
    print("YES")
else:
    print("NO")
