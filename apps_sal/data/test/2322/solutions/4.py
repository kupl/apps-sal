y, x = list(map(int, input().split()))
m = ['.'*(x+2)]
e = ''
try:
    for i in range(y):
        m.append('.'+input()+'.')
        a = m[i+1].find('S')
        if a != -1:
            b = [i+1, a]
except:
    pass
m.append('.'*(x+2))
a = [b[0], b[1]]
if m[a[0]-1][a[1]] == '*':
    e += ('U')
    a = [(a[0]-1), a[1]]
elif m[a[0]][a[1]-1] == '*':
    e += ('L')
    a = [a[0], a[1]-1]
elif m[a[0]+1][a[1]] == '*':
    e += 'D'
    a = [a[0]+1, a[1]]
else:
    e += 'R'
    a = [a[0], a[1]+1]
while a != b:
    if ((m[a[0]-1][a[1]] == '*') or (m[a[0]-1][a[1]] == 'S')) and e[-1] != 'D':
        e += ('U')
        a = [(a[0]-1), a[1]]
    elif ((m[a[0]][a[1]-1] == '*') or (m[a[0]][a[1]-1] == 'S')) and e[-1] != 'R':
        e += ('L')
        a = [a[0], a[1]-1]
    elif ((m[a[0]+1][a[1]] == '*') or (m[a[0]+1][a[1]] == 'S')) and e[-1] != 'U':
        e += 'D'
        a = [(a[0]+1), a[1]]
    else:
        e += 'R'
        a = [a[0], a[1]+1]
print(e)

