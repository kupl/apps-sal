class Solution:
    def maxSatisfaction(self, satisfaction) -> int:
        n = satisfaction.__len__()
        if n == 0:
            return 0
        satisfaction.sort()
        if satisfaction[-1] <= 0 :
            return 0
        else:
            mannux = 0
            while satisfaction:
                tem = 0
                for i in range(n):
                    tem += (i+1)*satisfaction[i]
                if mannux< tem:
                    mannux= tem
                satisfaction.pop(0)
                n -= 1
            return mannux
