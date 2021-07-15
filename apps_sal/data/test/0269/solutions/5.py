s = input()
a = s.find('R') % 4
b = s.find('B') % 4
c = s.find('Y') % 4
d = s.find('G') % 4
res = [0] * 4
for i in range(len(s)):
    if s[i] == '!':
        res[i % 4] += 1
print(res[a], res[b], res[c], res[d])
