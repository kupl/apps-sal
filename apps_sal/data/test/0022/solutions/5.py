s = input()

p = 'aBCcDEeFfGghiJjKkLlmNnPQRrSstuyZz'

for c in s:
    if c in p:
        print('NIE')
        return

def trans(c):
    d = {
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p',
    }
    if c in d:
        return d[c]
    return c

t = ''.join(map(trans, s[::-1]))
if t == s:
    print('TAK')
else:
    print('NIE')

