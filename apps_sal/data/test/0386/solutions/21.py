d = {
    '> Y': (0, 1, max),
    '>= Y': (0, 0, max),
    '< N': (0, 0, max),
    '<= N': (0, 1, max),
    '< Y': (1, -1, min),
    '<= Y': (1, 0, min),
    '> N': (1, 0, min),
    '>= N': (1, -1, min),
}
ran = [-2000000000, 2000000000]


def analyse(s):
    ls = s.split(' ')
    op = d.get(' '.join((ls[0], ls[2])))
    ran[op[0]] = op[2](int(ls[1]) + op[1], ran[op[0]])


n = int(input())
for i in range(n):
    s = input()
    if ran[0] <= ran[1]:
        analyse(s)

if ran[0] <= ran[1]:
    print(ran[0])
else:
    print('Impossible')
