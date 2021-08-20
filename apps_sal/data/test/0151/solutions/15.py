good = ['a', 'e', 'i', 'o', 'u']
s = input().strip()
ans = []
nw = ''
i = 0
while i < len(s) - 2:
    nw += s[i]
    if not s[i] == s[i + 1] == s[i + 2]:
        if not (s[i] in good or s[i + 1] in good or s[i + 2] in good):
            nw += s[i + 1]
            ans.append(nw)
            i += 1
            nw = ''
    i += 1
ans.append(nw + s[i:])
print(' '.join(ans))
