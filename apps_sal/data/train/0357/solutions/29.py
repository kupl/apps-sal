class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l_0 = 0
        begin_end_0 = -1
        curr = 0
        n = len(seats)
        for i, num in enumerate(seats):
            if num==0:
                curr += 1
                l_0 = max(curr, l_0)
            else:
                curr = 0
            if i == n-1 or i - curr + 1 == 0:
                begin_end_0 = max(begin_end_0,curr)
        return max(begin_end_0, (l_0-1)//2+1)

