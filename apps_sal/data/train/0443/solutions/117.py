class Solution:
    def numTeams(self, rat: List[int]) -> int:
        if(len(rat) < 3):
            return 0
        else:
            c = 0
            for i in range(len(rat)):
                for j in range(i + 1, len(rat)):
                    for k in range(j + 1, len(rat)):
                        if(rat[i] > rat[j] > rat[k]):
                            c += 1
            rat.reverse()
            for i in range(len(rat)):
                for j in range(i + 1, len(rat)):
                    for k in range(j + 1, len(rat)):
                        if(rat[i] > rat[j] > rat[k]):
                            c += 1
            return c
