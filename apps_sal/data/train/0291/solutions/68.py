"""
https://www.youtube.com/watch?v=iTukzycJ69I
"""


class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        """
            here we are calculating prefix sum.
            Along with that we also keep track before
            any index i, how many prefix sum are even 
            and how many prefix sum are odd by using
            variables evenSum and oddSum. Becuase if 
            we subtract 

            *************************************
                even value from odd answer is odd
                and odd value from even again answer
                is odd
            *************************************

            This above mentioned simple 2 rules helpsto
            keep track of required answer


        """
        evenSum = 0
        oddSum = 0
        prefSum = 0
        ans = 0
        for ele in arr:
            prefSum = prefSum + ele
            '\n                prefix sum is odd\n            '
            if prefSum % 2 == 1:
                ans += evenSum + 1
                oddSum += 1
            else:
                ans += oddSum
                evenSum += 1
            ans %= 10 ** 9 + 7
        return ans
