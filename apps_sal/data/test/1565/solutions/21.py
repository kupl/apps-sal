l = int(input())
s = input()
mi = int(s)
c = 0
for i in range(int(l / 2 + 1), l):
    if s[i] == '0':
        continue
    n1 = int(s[:i])
    n2 = int(s[i:])
    mi = min(mi, n1 + n2)
    c += 1
    if c >= 2:
        break
c = 0
for i in range(int(l / 2), 0, -1):
    if s[i] == '0':
        continue
    n1 = int(s[:i])
    n2 = int(s[i:])
    mi = min(mi, n1 + n2)
    break
    c += 1
    if c >= 2:
        break
print(mi)
