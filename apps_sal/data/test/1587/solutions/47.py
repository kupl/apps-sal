n = int(input())
s = str(input())
r = 0
w = 0
d = 0
for i in range(n):
    if s[i] == 'R':
        r += 1
    else:
        w += 1
sd = sorted(s)
for i in range(n):
    if s[i] != sd[i]:
        d += 1
if w == 0 or r == 0:
    print(0)
else:
    print(min(r, w, int(d / 2)))
