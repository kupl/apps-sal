s = input()
if len(s) % 2 == 1:
    c = 1
else:
    c = -1
s1 = ''
while len(s) > 0:
    if c > 0:
        s1 += s[0]
        s = s[1:]
    else:
        s1 += s[-1]
        s = s[: len(s) - 1]
    c *= -1
s2 = ''
for i in range(len(s1) - 1, -1, -1):
    s2 += s1[i]
print(s2)

