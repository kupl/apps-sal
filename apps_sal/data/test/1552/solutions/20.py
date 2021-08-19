i2 = input().split()
i1 = input().split()
i = 0
aa = i1.count('1')
b = i1.count('2')
c = i1.count('3')
g = min(aa, b, c)
print(g)
t = 0
while t < g:
    r = i1.index('1')
    i1[r] = 5
    r2 = i1.index('2')
    i1[r2] = 5
    r3 = i1.index('3')
    i1[r3] = 5
    print(r + 1, r2 + 1, r3 + 1)
    t = t + 1
