n = input()
s = 0
s += n.count('Danil')
s += n.count('Olya')
s += n.count('Slava')
s += n.count('Ann')
s += n.count('Nikita')
if s == 1:
    print('YES')
else:
    print('NO')
