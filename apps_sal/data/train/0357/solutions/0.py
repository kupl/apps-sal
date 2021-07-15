class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0 
        for seat, group in itertools.groupby(seats):
            if not seat:
                k = len(list(group))
                ans = max(ans, (k+1)//2)
        return max(ans, seats.index(1),seats[::-1].index(1))
        

