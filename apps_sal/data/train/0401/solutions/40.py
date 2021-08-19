
# 1262. Greatest Sum Divisible by Three

# Explanation: seen[i] means the current maximum possible sum that sum % 3 = i
# Complexity: Time O(N), Space O(1)

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for a in nums:
            for i in seen[:]:
                seen[(i + a) % 3] = max(seen[(i + a) % 3], i + a)
                # print(a, i, seen)
        return seen[0]
