#!/usr/bin/env python

def main( ):
    n = int( input( ) )
    w = list( map( int, input( ).split( ) ) )
    w100, w200 = w.count( 100 ), w.count( 200 )

    for i in range( w100 + 1 ):
        for j in range( w200 + 1 ):
            if i + 2 * j == w100 - i + 2 * w200 - 2 * j:
                print( "YES" )
                return
    print( "NO" )

def __starting_point():
    main( )


__starting_point()
