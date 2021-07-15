class Solution:
    def numTeams(self, r: List[int]) -> int:
        # we can do this in brute force with n^3
        
        # trivially impossible if fewer than 3 soldiers
        if len(r) < 3:
            return 0
        
        teams = 0
        
        # brute force
        
        for i in range(0, len(r) - 2):
            for j in range(i + 1, len(r) - 1):
                if i >= j:
                    break
                for k in range(j + 1, len(r)):
                    if j >= k:
                        break
                        
                    if r[i] < r[j] < r[k] or r[i] > r[j] > r[k]:
                        teams += 1
        return teams
