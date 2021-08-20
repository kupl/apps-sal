n = int(input())
s = list(input())
c0 = 0
c1 = 0
z0 = 0
z1 = 0
for i in range(n):
    if s[i] == '(':
        c0 += 1
    elif c0 > 0:
        c0 -= 1
    else:
        c1 += 1
z0 = c1
s = s[::-1]
c0 = 0
c1 = 0
for i in range(n):
    if s[i] == ')':
        c0 += 1
    elif c0 > 0:
        c0 -= 1
    else:
        c1 += 1
z1 = c1
s = s[::-1]
ans = ['('] * z0 + s + [')'] * z1
print(''.join(ans))
