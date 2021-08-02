def cnt(string, substr):
    return len(string.split(substr)) - 1


string = input()
x = 0

for i in ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']:
    x += cnt(string, i)

if (x == 1):
    print('YES')
else:
    print('NO')
