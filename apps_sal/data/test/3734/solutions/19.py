s1 = input()
s2 = input()
d = dict()
d['monday'] = 1
d['tuesday'] = 2
d['wednesday'] = 3
d['thursday'] = 4
d['friday'] = 5
d['saturday'] = 6
d['sunday'] = 0
if (d[s1] + 31 % 7) % 7 == d[s2] or (d[s1] + 30 % 7) % 7 == d[s2] or (d[s1] + 28 % 7) % 7 == d[s2]:
    print('YES')
else:
    print('NO')
