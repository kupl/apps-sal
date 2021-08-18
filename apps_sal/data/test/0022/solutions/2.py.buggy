d = {
    'A': 'A',
    'b': 'd',
    'd': 'b',
    'H': 'H',
    'I': 'I',
    'M': 'M',
    'O': 'O',
    'o': 'o',
    'X': 'X',
    'x': 'x',
    'Y': 'Y',
    'W': 'W',
    'V': 'V',
    'w': 'w',
    'v': 'v',
    'T': 'T',
    'p': 'q',
    'q': 'p',
    'U': 'U'
}
def g(c): return '*' if c not in list(d.keys()) else d[c]


s = input()
for i in range(len(s)):
    if s[i] != g(s[len(s) - i - 1]):
        print('NIE')
        return
print('TAK')
