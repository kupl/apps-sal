class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        validNumbers = {(1, i): 1 for i in range(10)}  # because it will always be 1 thing possible regardless of start digit. If we had used base case of 0, we would've gotten that we would double count. So sometimes it is better to do the simplest nontrivial basecase rather than try to work with 0.
        BIG_MOD = 10**9 + 7

        def computePhoneNumbers(length, startDigit):  # we can assume length is always >= 1
            if (length, startDigit) in validNumbers:
                return validNumbers[(length, startDigit)]
            else:
                totalValid = 0
                for neighbor in neighbors[startDigit]:
                    totalValid += computePhoneNumbers(length - 1, neighbor)
                    totalValid %= (BIG_MOD)
                validNumbers[(length, startDigit)] = totalValid
                return totalValid
        allValid = 0
        for i in range(10):
            allValid += computePhoneNumbers(n, i)
            allValid %= (BIG_MOD)
        return allValid
