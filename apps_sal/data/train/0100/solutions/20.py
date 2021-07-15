for _ in range(int(input())):
    l =list( map( int, input().split()) )
    l.sort()
    s, m , b = l
    a = s
    c = min( s, b - m )
    s -= c
    b -= c
    b -= s // 2
    m -= s - s // 2
    a += min( m, b )
    print( a )


