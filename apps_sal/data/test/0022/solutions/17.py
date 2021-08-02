s = input()

mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
while len(s) > 1:
    if s[0] in 'AoOIMHTUVvWwXxY':
        if s[0] == s[-1]: s = s[1:-1:]
        else: break
    elif s[0] in mirror:
        if s[0] == mirror[s[-1]]: s = s[1:-1:]
        else: break
    else: break

if len(s) == 0 or (s[0] in 'AoOIMHTUVvWwXxY' and len(s) == 1):
    print('TAK')
else: print('NIE')
