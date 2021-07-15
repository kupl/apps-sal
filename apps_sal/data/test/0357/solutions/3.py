arr = ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']
s = input()
c = 0
for i in arr:
    if i in s:
        c += s.count(i)
if c == 1:
    print('YES')
else:
    print('NO')

