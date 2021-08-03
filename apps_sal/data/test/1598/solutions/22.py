line = input()
res = []
zer = 0
one = 0

for i in range(len(line)):
    ind = len(line) - 1 - i

    if line[ind] == '0':
        res.append('0')
        zer += 1
    else:
        if zer <= one:
            res.append('0')
            zer += 1
        else:
            res.append('1')
        one += 1


for i in range(len(res)):
    print(res[len(res) - 1 - i], end='')
print('\n', end='')
