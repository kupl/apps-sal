ns = ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']
s = input()
res = 0
for i in ns:
    res += s.count(i)
print('YES' if res == 1 else 'NO')
