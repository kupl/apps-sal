s = list(input())
l = int(len(s))

m = []
for i in range(0, l, 2):
    m.append(s[i])
print((''.join(m)))
