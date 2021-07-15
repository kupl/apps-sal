def __starting_point():

    n , b , p = map( int , input().split() )

    res2 = n*p
    res1 = 0
    while n > 1:
        res1 += (n//2)*(2*b+1)
        n -= n//2

    print( res1 , res2 )
__starting_point()
