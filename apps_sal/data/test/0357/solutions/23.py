s = input()
a = 0
for t in ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']:
    a += s.count(t)
if a == 1:
    print('YES')
else:
    print('NO')
