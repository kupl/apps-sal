sl = 'AHIMOoTUVvWwXxY'
s = input()
n = len(s)
for i in range((n + 1) // 2):
    a, b = s[i], s[n - i - 1]
    if a == b and a in sl:
        continue
    elif sorted(a + b) in [['b', 'd'], ['p', 'q']]:
        continue
    else:
        print('NIE')
        return
print('TAK')
