t = input()
(s, d) = (0, 1)
p = {str(i): str(9 - i) for i in range(10)}
for i in range(len(t) - 1):
    if p[t[i]] == t[i + 1]:
        s += 1
    elif s:
        if s % 2 == 0:
            d *= s // 2 + 1
        s = 0
if s % 2 == 0:
    d *= s // 2 + 1
print(d)
