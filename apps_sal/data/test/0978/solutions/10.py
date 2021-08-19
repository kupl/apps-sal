k = int(input())
p = {i: 0 for i in '123456789.'}
for i in range(4):
    for j in input():
        p[j] += 1
p['.'] = 0
print('YNEOS'[max(p.values()) > 2 * k::2])
