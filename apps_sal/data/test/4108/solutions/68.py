s = input()
t = input()
n = len(s)
x = []
y = []

for i in range(n):
    if s[i] not in x:
        x.append(s[i])
    if t[i] not in y:
        y.append(t[i])

for i in range(len(x)):
    s = s.replace(x[i], str(i))
for i in range(len(y)):
    t = t.replace(y[i], str(i))
print('Yes' if s == t else 'No')
