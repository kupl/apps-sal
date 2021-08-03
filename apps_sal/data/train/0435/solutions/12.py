class Solution(object):
    def subarraysDivByK(self, A, K):
        nums = A
        k = K
        modDict = {}
        tempSumn = 0
        ans = 0
        continousSum = []

        for num in nums:
            tempSumn += num
            continousSum.append(tempSumn)
            remain = tempSumn % k

            if remain not in modDict:
                modDict[remain] = 0
            modDict[remain] += 1

        diff = k
        for i in range(0, len(continousSum)):
            if diff % k in modDict:
                ans += modDict[diff % k]

            diff = continousSum[i]
            modDict[diff % k] -= 1

        return ans
