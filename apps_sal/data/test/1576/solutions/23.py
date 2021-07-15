s = input()
side = -1
if len(s) % 2 == 1:
    side = 0
o = ''
for i in range(len(s)):
    o += s[side]
    if side == -1:
        s = s[:-1]
        side = 0
    else:
        s = s[1:]
        side = -1

for i in range(len(o) - 1, -1, -1):
    print(o[i], end='')

