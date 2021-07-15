__author__ = 'asmn'

n = int(input())
a = sorted((num, (j, i)) for i in range(n) for (j, num) in enumerate(map(int, input().split())))
mk = [['0'] * n, ['0'] * n]

for (k, (num, (j, i))) in enumerate(a):
    if (i + 1) * 2 <= n or (k + 1) <= n:
        mk[j][i] = '1'

print('\n'.join(''.join(ss) for ss in mk))


