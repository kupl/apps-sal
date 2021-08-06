t = input()
s = input()
l_t = len(t)
l_s = len(s)
x = 0
f = l_s + 1
for i in range(l_s):
    if t[x] == s[i]:
        x += 1
    if x == l_t:
        f = i
        break
c = -1
y = l_t - 1
for i in range(l_s - 1, -1, -1):
    if t[y] == s[i]:
        y -= 1
    if y == -1:
        c = i
        break
if c - f <= 0:
    print(0)
else:
    print(c - f)
