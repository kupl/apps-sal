s = (input())

s2 = ""
p = -1
s += "11"
for i in range(len(s) - 2):
    if (s[i] != '1' or s[i + 1] != '4' or s[i + 2] != '4') and (i > p):
        s2 += s[i]
    else:
        if p < i:
            p = i + 2
            s2 += '*'
p = -1
s = s2
s2 = ""
s += "11"
for i in range(len(s) - 1):
    if (s[i] != '1' or s[i + 1] != '4') and (i > p):
        s2 += s[i]
    else:
        if p < i:
            p = i + 1
            s2 += '*'
p = -1
s = s2
s2 = ""

for i in range(len(s)):
    if s[i] != '1':
        s2 += s[i]
s = s2
for i in range(len(s)):
    if s2[i] != '*':
        print("NO")
        return
print("YES")
