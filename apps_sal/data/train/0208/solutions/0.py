class Solution:
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        num = 0
        while ('R' in senate and 'D' in senate):
            res = []
            for i in senate:
                if i == 'R':
                    if num >= 0:
                        res.append(i)
                    num += 1
                else:
                    if num <= 0:
                        res.append(i)
                    num -= 1
            senate = res
        return 'Radiant' if 'R' in senate else 'Dire'
