class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        currmax = 0
        satsort = sorted(satisfaction)
        leng1 = len(satsort)
        
        for nn in range(leng1):
            satpart = satsort[nn:]
            leng2 = leng1 - nn
            time = [ii for ii in range(1, leng2 + 1)]
            
            coeff = []
            for ii in range(leng2):
                coeff.append(satpart[ii] * time[ii])
            cumul = [coeff[0]]
            for ii in range(1, leng2):
                cumul.append(cumul[ii - 1] + coeff[ii])
            for elem in cumul:
                if currmax < elem:
                    currmax = elem
        return currmax
