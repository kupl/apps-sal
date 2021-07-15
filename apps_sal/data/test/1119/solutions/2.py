import math
import sys

k, pa, pb = list( map( int, input().split() ) )


memo = {}

sys.setrecursionlimit(1500*1500*2)

MOD = (10**9 + 7 )

def pow( a, b ):

    ret = 1

    while b > 0:

        if b & 1:
            ret = (ret*a)%MOD

        a = (a*a)%MOD

        b //= 2

    return ( ret )

def inv(a):
   return pow( a, MOD-2 )

Pa = pa * inv( pa + pb )
Pb = pb * inv( pa + pb )
pa_inv_pb = pa * inv(pb)

def f( total_a, total_ab ):

    if total_a+total_ab >= k:
        return total_a+total_ab + pa_inv_pb

    if (total_a,total_ab) in memo:
        return memo[ (total_a,total_ab) ]

    Best = 0

    Best += Pa * f( total_a+1, total_ab )
    Best %= MOD

    Best += Pb * f( total_a, total_a+total_ab )
    Best %= MOD

    memo[ (total_a,total_ab) ] = Best

    return ( Best )

#print( k, pa, pb )

print( ( f(1,0) ) % MOD )

