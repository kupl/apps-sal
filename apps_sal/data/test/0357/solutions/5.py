s = input()
l = ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']
ans = 0
for i in l:
    ans += s.count(i)
if ans != 1:
    print('NO')
else:
    print('YES')
