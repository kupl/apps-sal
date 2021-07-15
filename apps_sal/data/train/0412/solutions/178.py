class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9 + 7
        state = [ 1 ] + [ 0 ] * ( target )
        for i in range( d ) :
            for j in range( target , -1 , -1 ) :
                state[ j ] = 0
                for k in range( 1 , min( f , j ) + 1 ) :
                    state[ j ] += state[ j - k ]
                    state[ j ] %= mod
        return state[-1]
#Sanyam Rajpal

