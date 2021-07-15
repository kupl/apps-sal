s = input()
l = ['?','?','?','?']
d = {c:0 for c in "RGBY"}
for i in range(len(s)):
    if s[i] != '!':
        l[i%4] = s[i]
for i in range(len(s)):
    if s[i] == '!':
        d[l[i%4]] += 1

print(d['R'],d['B'],d['Y'],d['G'])

