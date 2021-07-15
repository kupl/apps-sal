n, k = map(int, input().split())
s = input()

n, s = 2 * n, 2 * s
for _ in range(k):
    tmp = []
    for i in range(0, n, 2):
        if s[i] == s[i + 1]:
            tmp.append(s[i])
        else:
            comb = sorted([s[i], s[i + 1]])
            if comb == ['P', 'R']:
                tmp.append('P')
            elif comb == ['R', 'S']:
                tmp.append('R')
            else:
                tmp.append('S')
    s = ''.join(2 * tmp)
print(s[0])
