s = str(input())
a = []

for i in range(len(s)):
    if s[i] == '0':
        a.append('0')
    elif s[i] == '1':
        a.append('1')
    else:
        if len(a) != 0:
            a.pop()

print(''.join(a))
