s = list(input())
x = len(s)
a = []
for i in range(x):
    if s[i] == '0':
        a.append('0')
    elif s[i] == '1':
        a.append('1')
    elif s[i] == 'B':
        if a == []:
            continue
        else:
            a.pop(-1)
b = ''.join(a)
print(b)
