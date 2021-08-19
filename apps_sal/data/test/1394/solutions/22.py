t = input()
s = ''
for elem in t:
    if elem != 'a':
        s += elem
if len(s) % 2 != 0:
    print(':(')
else:
    c = len(s) // 2
    if c == 0:
        print(t)
    elif s[:c] != s[c:]:
        print(':(')
    elif t[-c:] != s[c:]:
        print(':(')
    else:
        print(t[:-c])
