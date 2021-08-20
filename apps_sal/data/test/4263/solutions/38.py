s = input()
ans = 0
zantei = 0
for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or (s[i] == 'T'):
        zantei += 1
    else:
        ans = max(ans, zantei)
        zantei = 0
ans = max(ans, zantei)
print(ans)
