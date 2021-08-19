input()
s = input()
c = 0
for i in s:
    if i == '(':
        c += 1
    elif c > 0:
        c -= 1
d = 0
for i in s[::-1]:
    if i == ')':
        d += 1
    elif d > 0:
        d -= 1
print('(' * d + s + ')' * c)
