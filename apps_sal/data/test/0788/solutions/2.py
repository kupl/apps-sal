s = input()
pr = 0
ss = 0
for i in range(1, len(s)):
    if (s[i] == '0'):
        pr *= 10

    ss += pr
    pr = int(s[i])
ss += pr
print(ss + 1)
