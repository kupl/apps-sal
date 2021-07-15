import sys
M = int( 1e9 ) + 7
def I():
    return sys.stdin.readline().rstrip()

s = I()

if 'w' in s or 'm' in s:
    print( 0 )
else:
    f = [ 1, 1 ]
    for i in range(len(s)):
        f.append( ( f[ -1 ] + f[ -2 ] ) % M )
    sm = []
    last = 'k'
    for c in s:
        if c in 'un':
            if last != c:
                sm.append( 1 )
            else:
                sm[ -1 ] += 1
        last = c
    ans = 1
    for i in sm:
        ans *= f[ i ]
        ans %= M
    print( ans )

