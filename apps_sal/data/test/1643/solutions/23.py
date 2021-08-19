s = input()
s = list(s)
l = len(s) - 1
z = 0
for i in range(l, -1, -1):
    if s[i] == '0':
        z += 1
    elif z:
        z -= 1
    else:
        s[i] = '0'
s = ''.join(s)
print(s)
