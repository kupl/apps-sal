from functools import lru_cache

@lru_cache
def find_ns( rating, i, n, bigger ):
    res = []
    while i < len( rating ):
        if bigger and rating[i] > n or not bigger and rating[i] < n:
            res.append( i )
        i += 1
    return res
        

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        rating = tuple( rating )
        i = 0
        num_teams = 0
        while i < len(rating)-2:
            for i2 in find_ns( rating, i+1, rating[i], True ):
                for i3 in find_ns( rating, i2+1, rating[i2], True ):
                    num_teams += 1
            for i2 in find_ns( rating, i+1, rating[i], False ):
                for i3 in find_ns( rating, i2+1, rating[i2], False ):
                    num_teams += 1
            i += 1
        return num_teams

