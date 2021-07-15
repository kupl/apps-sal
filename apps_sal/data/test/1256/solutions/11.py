s = list(map(int, input().split('+')))
s.sort()
print(s[0], end='')
for i in s[1:]:
    print('+', i, end='', sep='')

