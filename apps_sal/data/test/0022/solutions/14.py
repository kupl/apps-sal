d = {'A': 'A',
     'b': 'd',
     'd': 'b',
     'H': 'H',
     'I': 'I',
     'M': 'M',
     'O': 'O',
     'o': 'o',
     'p': 'q',
     'q': 'p',
     'T': 'T',
     'U': 'U',
     'V': 'V',
     'v': 'v',
     'W': 'W',
     'w': 'w',
     'X': 'X',
     'x': 'x',
     'Y': 'Y'}
s = input()

f = True

if len(s) % 2 == 0:
    l = s[:len(s) // 2]
    r = s[len(s) // 2:]
else:
    l = s[:len(s) // 2]
    if s[len(s) // 2] not in d or d[s[len(s) // 2]] != s[len(s) // 2]:
        f = False
    r = s[len(s) // 2 + 1:]

r = list(r)
for i in range(len(r)):
    if r[i] not in d:
        f = False
    else:
        r[i] = d[r[i]]

if r[::-1] == list(l) and f:
    print("TAK")
else:
    print("NIE")
