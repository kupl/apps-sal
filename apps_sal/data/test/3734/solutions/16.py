d = dict()
d['monday'] = 0
d['tuesday'] = 1
d['wednesday'] = 2
d['thursday'] = 3
d['friday'] = 4
d['saturday'] = 5
d['sunday'] = 6
s1 = input()
s2 = input()
x = (d[s2] - d[s1] + 7) % 7
if x == 0 or x == 2 or x == 3:
    print('YES')
else:
    print('NO')
