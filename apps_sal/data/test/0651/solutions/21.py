
import itertools
n, m = map(int, input().split())


def road(ins):
    cur = S.copy()
    for x in s:
        x = int(x)
        if ar[cur[0]][cur[1]] == 'E':
            return 1
        if ins[x] == 'U':
            try:
                if ar[cur[0] + 1][cur[1]] != '
                cur = [cur[0] + 1, cur[1]]
                else:
                    return 0
            except:
                return 0
        if ins[x] == 'D':
            try:
                if ar[cur[0] - 1][cur[1]] != '
                cur = [cur[0] - 1, cur[1]]
                else:
                    return 0
            except:
                return 0
        if ins[x] == 'R':
            try:
                if ar[cur[0]][cur[1] + 1] != '
                cur = [cur[0], cur[1] + 1]
                else:
                    return 0
            except:
                return 0
        if ins[x] == 'L':
            try:
                if ar[cur[0]][cur[1] - 1] != '
                cur = [cur[0], cur[1] - 1]
                else:
                    return 0
            except:
                return 0
    if ar[cur[0]][cur[1]] == 'E':
        return 1
    else:
        return 0


ar = [input() for x in range(n)]
S = [0, 0]
E = [0, 0]
for x in range(n):
    if 'S' in ar[x]:
        S = [x, ar[x].index('S')]
    if 'E' in ar[x]:
        E = [x, ar[x].index('E')]
s = input()
i = 0
for x in list(itertools.permutations(['U', 'D', 'L', 'R'])):
    i += road(list(x))
print(i)
