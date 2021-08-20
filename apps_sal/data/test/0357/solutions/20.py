s = input()
ls = ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']
c = 0
for n in ls:
    c += s.count(n)
if c == 1:
    print('YES')
else:
    print('NO')
