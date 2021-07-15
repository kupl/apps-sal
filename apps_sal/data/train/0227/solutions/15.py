class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ans , i , c = 0 , 0 , [ ]
        for j in range( len( A ) ) :
            if A[ j ] == 0 :
                c += j ,
            while len( c ) > K :
                 i = c.pop( 0 ) + 1
            ans = max( ans , j - i + 1 )
        return ans
#Sanyam Rajpal

