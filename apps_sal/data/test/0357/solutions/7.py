l = ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']
s = input()
d = 0
for i in l:
    d += s.count(i)
print('YES' if d == 1 else 'NO')
