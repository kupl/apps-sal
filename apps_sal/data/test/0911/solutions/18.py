'__author__' == 'deepak Singh Mehta'


def __starting_point():
    (n, c) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    t = list(map(int, input().split()))
    limak = 0
    eff = 0
    for i in range(len(p)):
        eff += t[i]
        limak += max(0, p[i] - eff * c)
    rade = 0
    eff = 0
    for i in range(len(p) - 1, -1, -1):
        eff += t[i]
        rade += max(0, p[i] - eff * c)
    if limak > rade:
        print('Limak')
    elif limak < rade:
        print('Radewoosh')
    else:
        print('Tie')


__starting_point()
