s = input()
g = ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']
c = 0
for i in g:
    c += s.count(i)
if c == 1:
    print('YES')
else:
    print('NO')
