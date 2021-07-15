class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sat_sort = sorted(satisfaction)
        max_sat = 0
        for i in range(len(sat_sort)):
            sat = sum(t*s for t, s in enumerate(sat_sort[i:],start=1))
            max_sat = max(max_sat,sat,0)
        return max_sat

