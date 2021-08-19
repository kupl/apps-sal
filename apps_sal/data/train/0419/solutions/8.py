class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bulbs = [False] * n;
        # for i in range(0,int(n/2)+1):
        #     j = i+1;
        #     for j in range(i,n,j):
        #         bulbs[j] = True if bulbs[j] is False else False;
        #     print(bulbs,j)
        # return bulbs.count(True)
        return int(n**(1 / 2))
