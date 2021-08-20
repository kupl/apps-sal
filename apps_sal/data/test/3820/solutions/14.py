input()
s = input()
t = input()
if '*' not in s:
    print('YES' if s == t else 'NO')
else:
    (l, r) = s.split('*')
    if t.startswith(l) and t.endswith(r) and (len(l) + len(r) <= len(t)):
        print('YES')
    else:
        print('NO')
