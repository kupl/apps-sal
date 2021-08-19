(n, m) = list(map(int, input().split(' ')))
field = ''
k = 0
for i in range(n):
    if i % 2 == 0:
        field += '#' * m + '\n'
    elif k == 0:
        k = 1
        field += '.' * (m - 1) + '#' + '\n'
    else:
        k = 0
        field += '#' + '.' * (m - 1) + '\n'
print(field.strip())
