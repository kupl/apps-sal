class Solution:

    def numTeams(self, r: List[int]) -> int:
        ct = 0
        for i in range(len(r)):
            for j in range(i + 1, len(r)):
                b = -1
                if r[i] > r[j]:
                    b = 1
                else:
                    b = 0
                for k in range(j + 1, len(r)):
                    if b == 1 and r[k] < r[j]:
                        ct += 1
                        continue
                    if b == 0 and r[k] > r[j]:
                        ct += 1
                        continue
        return ct
