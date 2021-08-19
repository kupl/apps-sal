class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum = 0
        for num in A:
            sum += num
        if sum % 3 != 0:
            return False
        sum = sum / 3
        total = 0
        currentSum = 0
        for num in A:
            currentSum += num
            if currentSum == sum:
                total += 1
                currentSum = 0
        return True if total >= 3 else False
