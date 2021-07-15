qw = input()
g = ['*']
s = [1]
for i in range(len(qw)):
    if i % 2 == 0:
        s.append(int(qw[i]))
    else:
        g.append(qw[i])
c = 0
g.append('*')
s.append(1)
for i in range(len(g)):
    if g[i] == '*':
        for j in range(i + 1, len(g)):
            if g[j] == '*':
                a = 0
                b = s[0]
                for k in range(i):
                    if g[k] == '*':
                        b *= s[k + 1]
                    else:
                        a += b
                        b = s[k + 1]
                v = a
                w = b
                a = 0
                b = s[i + 1]
                for k in range(i + 1, j):
                    if g[k] == '*':
                        b *= s[k + 1]
                    else:
                        a += b
                        b = s[k + 1]
                b = w * (a + b)
                a = v
                for k in range(j, len(g)):
                    if g[k] == '*':
                        b *= s[k + 1]
                    else:
                        a += b
                        b = s[k + 1]
                c = max(c, a + b)
print(c)
