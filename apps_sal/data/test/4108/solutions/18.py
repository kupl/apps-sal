s = input()
t = input()
x = []
y = []
for i in range(len(s)):
    if s[i] not in x:
        x.append(s[i])
    if t[i] not in y:
        y.append(t[i])
for i in range(len(x)):
    s = s.replace(x[i], str(i))
for i in range(len(y)):
    t = t.replace(y[i], str(i))
if s == t:
    print("Yes")
else:
    print("No")
