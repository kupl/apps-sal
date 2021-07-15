from sys import stdin

s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()
ss = stdin.readline().rstrip()

data = {}
for i in range(0, len(s1)):
    data[s1[i]] = s2[i]
    data[s1[i].upper()] = s2[i].upper()

rs = []
for i in ss:
    rs.append(data[i] if i in data else i)

print(''.join(rs))

