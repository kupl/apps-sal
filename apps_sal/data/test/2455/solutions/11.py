from functools import reduce
print('\n'.join([(lambda x: '%i %s' % (len(x), ' '.join(x)))((lambda h: ['%ix%i' % (12 // i, i) for i in (12, 6, 4, 3, 2, 1) if reduce(lambda x, y: x & y, [int(h.replace('O', '0').replace('X', '1')[i * j:i * j + i], 2) for j in range(12 // i)], -1)])(input())) for i in range(int(input()))]))
