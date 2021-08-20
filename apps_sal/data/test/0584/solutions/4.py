n = int(input())
s = input().split('(')
t = []
for i in range(len(s)):
    t += s[i].split(')')
a = t[1::2]
b = t[::2]
(a1, b1) = (0, 0)
for i in b:
    for j in i.split('_'):
        a1 = max(a1, len(j))
for i in a:
    for j in i.split('_'):
        if j != '':
            b1 += 1
print(a1, b1)
