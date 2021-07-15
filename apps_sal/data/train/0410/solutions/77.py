class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = []
        for i in range(lo, hi+1):
            index = i
            steps = 0
            while i != 1: 
                if i % 2 == 0: 
                    i = i / 2
                    steps += 1
                else: 
                    i = 3 * i + 1
                    steps += 1
            powers.append([steps, index])         
        sortPowers = sorted(powers)
        return sortPowers[k-1][1]
