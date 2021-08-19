s = input()
a = ''
s = s[::-1]
o = 0
z = 0
i = 0
while i != len(s):
    if s[i] == '2':
        a = a + '0' * z + '2'
        z = 0
    if s[i] == '0':
        z += 1
    if s[i] == '1':
        o += 1
    i += 1
a = a + '1' * o + '0' * z
a = a[::-1]
print(a)
