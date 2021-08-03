class Solution:
    def maxDiff(self, num: int) -> int:

        maxi = '-inf'
        mini = 'inf'

        num = str(num)
        leading = num[0]

        for a in set(num):
            a = str(a)
            for b in range(10):

                if (not b) and (a == leading):
                    continue
                b = str(b)

                temp = num.replace(a, b)
                mini = min(mini, temp)
                maxi = max(maxi, temp)

        return int(maxi) - int(mini)
