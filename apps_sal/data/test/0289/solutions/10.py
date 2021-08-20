s = input()
m = s.count('VK')
for i in range(len(s)):
    s2 = s[:i] + 'V' + s[i + 1:]
    s3 = s[:i] + 'K' + s[i + 1:]
    m = max(m, s2.count('VK'))
    m = max(m, s3.count('VK'))
print(m)
