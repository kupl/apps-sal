class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [ [ 0 for _ in range( target + 1 ) ] for _ in range( d + 1 ) ]
        dp[ 0 ][ 0 ] = 1
        for i in range( d ) :
            for j in range( 1 , f + 1 ) :
                for k in range( target ) :
                    if k + j <= target :
                        dp[ i + 1 ][ k + j ] += dp[ i ][ k ]
                        dp[ i + 1 ][ k + j ] %= mod
        return dp[-1][-1]
#Sanyam Rajpal

