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
ans = ['('] * c1 + s + [')'] * c0
print(''.join(ans))
