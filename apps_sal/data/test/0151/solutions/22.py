s = input()
a = []
volumes = ['a', 'e', 'i', 'o', 'u']
i = 0
f = 0
while i + 2 < len(s):
    if s[i] not in volumes and s[i + 1] not in volumes and s[i + 2] not in volumes and (s[i] != s[i + 1] or s[i] != s[i + 2] or s[i + 1] != s[i + 2]):
        a.append(s[f:i + 2])
        f = i + 2
        i += 2
        continue
    i += 1
if len(a) == 0:
    print(s)
else:
    a.append(s[f:len(s)])
    print(" ".join(a))
