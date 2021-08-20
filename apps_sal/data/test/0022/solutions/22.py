s = input()
sym = 'AHIMOoTUVvWwXxY'
mir = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
ans = True
l = len(s)
if l % 2 != 0 and s[l // 2] not in sym:
    ans = False
else:
    for i in range(l // 2):
        if not (s[i] in mir and mir[s[i]] == s[l - i - 1] or (s[i] in sym and s[i] == s[l - i - 1])):
            ans = False
            break
print('TAK' if ans else 'NIE')
