from itertools import combinations
n = int(input())
d = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for i in range(n):
    s = input()
    if s[0] == 'M':
        d['M'] += 1
    if s[0] == 'A':
        d['A'] += 1
    if s[0] == 'R':
        d['R'] += 1
    if s[0] == 'C':
        d['C'] += 1
    if s[0] == 'H':
        d['H'] += 1
ans = 0
for (i, j, k) in combinations('MARCH', 3):
    ans += d[i] * d[j] * d[k]
print(ans)
