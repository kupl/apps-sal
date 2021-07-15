def solve( h , n ):

    sortedH = sorted(h)
    hsum = [0]
    for i in range(1,n+1):
        hsum.append( hsum[i-1] + sortedH[i-1] )

    tsum = 0
    start =0
    res = 0
    for i,hi in enumerate(h):
        tsum += hi
        if tsum == hsum[i+1]-hsum[start]:
            res += 1
            tsum = 0
            start = i + 1

    return res

def __starting_point():

    n = int( input() )
    h = [ int(x)-1 for x in input().split() ]

    print( solve( h , n ) )
__starting_point()
