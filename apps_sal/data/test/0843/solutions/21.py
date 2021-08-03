n, s, i = int(input()), input(), 0
d = list(map(int, input().split()))
for _ in range(len(s) + 1):
    if i < 0 or i >= len(s):
        print('FINITE')
        return
    i += [d[i], -d[i]][s[i] == '<']
print('INFINITE')
