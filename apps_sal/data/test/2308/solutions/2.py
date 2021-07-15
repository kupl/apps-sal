res = []
for TT in range(1, int(input()) + 1):
    a, b = input()[::-1], input()[::-1]
    i = b.index('1')
    j = a[i:].index('1')
    res.append(j)
print(*res, sep='\n')
