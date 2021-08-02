from functools import reduce
g = lambda a, b: g(b, a % b)if b else a
gcd = lambda x: reduce(g, x)
input()
*a, = list(map(int, input().split()))
b = gcd(a)
a = [i // b for i in a]
c = True
for i in a:
    while not i % 2: i //= 2
    while not i % 3: i //= 3
    if i != 1:
        c = False
        print('No')
        break
if c: print('Yes')
