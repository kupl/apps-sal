lim = 2 ** 32 - 1
n = int( input() )
ans = 0
f = [ 1 ]
a = [ 0 ]
ov = False
for l in range(n):
    i = input()
    if i == 'add':
        if a[ -1 ] < lim:
            a[ -1 ] += 1
        else:
            ov = True
            break
    elif i[ :3 ] == 'for':
        f.append( int(i[ 4: ]) )
        a.append( 0 )
    else:
        if a[ -1 ] == 0:
            f.pop()
            a.pop()
            continue
        if lim / f[ -1 ] < a[ -1 ]:
            ov = True
            break
        sm = f.pop() * a.pop()
        if lim - sm < a[ -1 ]:
            ov = True
            break
        a[ -1 ] += sm

if not ov:
    print( a[ -1 ] )
else:
    print( "OVERFLOW!!!")

