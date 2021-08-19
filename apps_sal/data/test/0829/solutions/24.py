n = input()
s = input()
z = 0
nz = 0
for i in s:
    if i == '0':
        z += 1
    else:
        nz += 1
if z != nz:
    print(1)
    print(s)
else:
    print(2)
    for i in range(len(s) - 1):
        print(s[i], end='')
    print(' ', end='')
    print(s[len(s) - 1])
