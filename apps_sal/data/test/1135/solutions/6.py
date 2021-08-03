# yl2 decode
n = int(input())
s = list(input())
med = s[len(s) // 2]
s0 = ''
if len(s) % 2 == 1:
    s0 += s.pop(0)
while len(s) != 0:
    s0 = s.pop(0) + s0
    s0 += s.pop(0)
print(s0)
