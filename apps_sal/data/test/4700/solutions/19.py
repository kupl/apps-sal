import sys
input = sys.stdin.readline

def main():
    n , m = map( int , input().split() )
    h = list( map( int , input().split() ) )
    goods = [ 1 for i in range(n) ]
    for i in range( m ):
        a , b = map( lambda x : int(x) - 1  , input().split() )
        if ( h[a] > h[b] ):
            goods[ b ] = 0
        if ( h[a] < h[b] ):
            goods[ a ] = 0
        if ( h[a] == h[b] ):
            goods[ a ] = 0
            goods[ b ] = 0
    print( sum(goods) )
main()
