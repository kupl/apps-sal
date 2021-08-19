s = input()
i = 0
a = s.find('VK')
ans = 0
while a != -1:
    ans += 1
    s = s[:a] + '.' + s[a + 2:]
    a = s.find('VK')
if s.count('VV') > 0 or s.count('KK') > 0:
    ans += 1
print(ans)
