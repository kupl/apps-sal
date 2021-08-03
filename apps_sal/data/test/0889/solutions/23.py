lst = []
for i in range(4):
    temp = input()
    lst.append(temp)

if '##' in lst[0]:
    temp = lst[0].index('##')
    if lst[1][temp] == '#' or lst[1][temp + 1] == '#':
        print('YES')
        return

for i in range(1, 3):
    if '##' in lst[i]:
        temp = lst[i].index('##')
        if lst[i - 1][temp] == '#' or lst[i - 1][temp + 1] == '#':
            print('YES')
            return
        if lst[i + 1][temp] == '#' or lst[i + 1][temp + 1] == '#':
            print('YES')
            return

if '##' in lst[3]:
    temp = lst[3].index('##')
    if lst[2][temp] == '#' or lst[2][temp + 1] == '#':
        print('YES')
        return

if '..' in lst[0]:
    temp = lst[0].index('..')
    if lst[1][temp] == '.' or lst[1][temp + 1] == '.':
        print('YES')
        return

for i in range(1, 3):
    if '..' in lst[i]:
        temp = lst[i].index('..')
        if lst[i - 1][temp] == '.' or lst[i - 1][temp + 1] == '.':
            print('YES')
            return
        if lst[i + 1][temp] == '.' or lst[i + 1][temp + 1] == '.':
            print('YES')
            return

if '..' in lst[3]:
    temp = lst[3].index('..')
    if lst[2][temp] == '.' or lst[2][temp + 1] == '.':
        print('YES')
        return

print('NO')
