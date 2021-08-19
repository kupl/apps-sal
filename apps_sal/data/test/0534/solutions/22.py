(n, t) = map(int, input().split())
s = [c for c in input()]
for i in range(t):
    skip = False
    for (j, n) in enumerate(s[:-1]):
        if skip == True:
            skip = False
            continue
        if s[j] == 'B' and s[j + 1] == 'G':
            (s[j], s[j + 1]) = ('G', 'B')
            skip = True
print(''.join((c for c in s)))
