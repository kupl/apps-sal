k = int(input())

if (k == 0):
    print('+')
    return

answer = [['+', '+'], ['+', '*']]
length = 2
for i in range(k - 1):
    new = []
    for i in answer:
        temp = []
        for j in range(length):
            if i[j] == '+':
                temp += ['+', '+']
            else:
                temp += ['*', '*']
        new.append(temp)
    for i in answer:
        temp = []
        for j in range(length):
            if i[j] == '+':
                temp += ['+', '*']
            else:
                temp += ['*', '+']
        new.append(temp)
    answer = new
    length *= 2

print('\n'.join([''.join(i) for i in answer]))
