class Solution:
    def numTeams(self, s: List[int]) -> int:
        count = 0
        if len(s) < 3:
            return 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                for k in range(j + 1, len(s)):
                    if s[i] < s[j] and s[j] < s[k]:
                        count += 1
                    if s[i] > s[j] and s[j] > s[k]:
                        count += 1
        return count   
