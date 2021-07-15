from collections import defaultdict as dd
d = dd(int)

n = int(input())
for i in range(n):
    s = input()
    f = 0
    ff = 0
    for j in range(len(s)):
        if s[ j ] == '(':
            f += 1
        elif s[ j ] == ')':
            f -= 1
        if f < 0:
            ff += 1
            f = 0
    if f == 0:
        d[ -ff ] += 1
    elif ff == 0:
        d[ f ] += 1

s = d[ 0 ] // 2
for k, v in list(d.items()):
    if k > 0:
        s += min( d[ k ], d[ -k ] )

print( s )



