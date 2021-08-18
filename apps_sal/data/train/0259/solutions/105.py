class Solution:
    def divide(self, num, divisor):
        return -((-num) // divisor)

    def getQuotient(self, nums, divisor):
        output = 0
        for num in nums:
            output += self.divide(num, divisor)
        return output

    def getResult(self, results, divisor, nums):
        if divisor in results:
            return results[divisor]
        else:
            results[divisor] = self.getQuotient(nums, divisor)
            return results[divisor]

    def helper(self, results, nums, i, j, threshold):
        if i == j:
            return i

        mid = (i + j) // 2
        if mid == 1:
            return mid
        elif self.getResult(results, mid, nums) <= threshold and self.getResult(results, mid - 1, nums) > threshold:
            return mid
        elif self.getResult(results, mid, nums) <= threshold:
            return self.helper(results, nums, i, mid - 1, threshold)
        else:
            return self.helper(results, nums, mid + 1, j, threshold)

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        maxDivisor = self.divide(2 * sum(nums), threshold)
        results = dict()

        return self.helper(results, nums, 1, maxDivisor, threshold)
