insym = set(('A', 'H', 'I', 'M', 'O', 'o', 'T', 'U', 'V', 'v', 'W', 'w', 'X', 'x', 'Y'))
disym = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
for c in insym:
    disym[c] = c
s = input()
n = len(s)
if n % 2 == 0 or s[n // 2] in insym:
    s1 = s[0:n // 2]
    s2 = s[::-1][0:n // 2]
    flg = True
    for i in range(n // 2):
        if s1[i] not in disym or disym[s1[i]] != s2[i]:
            flg = False
    if flg:
        print('TAK')
    else:
        print('NIE')
else:
    print('NIE')
