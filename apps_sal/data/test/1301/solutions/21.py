n = int(input())
name = input()
if n == 6:
    print('espeon')
elif n == 8:
    print('vaporeon')
else:
    names = ['jolteon', 'flareon', 'umbreon', 'leafeon', 'glaceon', 'sylveon']
    flag = [1] * 6
    for i in range(6):
        for j in range(7):
            if names[i][j] != name[j] and name[j] != '.':
                flag[i] = 0
    for i in range(6):
        if flag[i] == 1:
            print(names[i])
            break
