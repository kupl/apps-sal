T = int(input())
for _ in range(T):
    n, a, b = list(map( int, input().split() ))
    s = input()
    ans = n * a + ( n + 1 ) * b
    li = s.find('1')
    if li >= 0:
        ri = s.rfind('1')
        ans += a + a + ( ri - li + 2 ) * b
        lens = []
        for i in range( li + 1, ri ):
            if s[ i ] == '0':
                if( s[ i - 1 ] == '1' ):
                    lens.append(0)
                lens[-1] += 1
        for l in lens:
            sm = a + a - ( l - 1 ) * b
            if l > 1 and sm < 0:
                ans += sm
    print( ans )


