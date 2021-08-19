def alternate(c):
    if c == 'V':
        return 'K'
    return 'V'


s = input()
res = s.count('VK')
for i in range(len(s)):
    res = max(res, (s[:i] + alternate(s[i]) + s[i + 1:]).count('VK'))
print(res)
