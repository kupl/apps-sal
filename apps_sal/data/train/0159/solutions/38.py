class MonoQ:

    def __init__(self, k):
        self.k = k
        self.m = []

    def add(self, a, solution):
        while len(self.m) > 0:
            if solution[a] > solution[self.m[-1]]:
                self.m.pop()
            else:
                break
        self.m.append(a)

    def grab(self, a, solution, nums):
        if len(self.m) > 0:
            if self.m[0] > a + self.k:
                self.m = self.m[1:]
            return max(nums[a], nums[a] + solution[self.m[0]])
        else:
            return nums[a]


class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        solution = [0] * n
        m = MonoQ(k)
        for i in range(n - 1, -1, -1):
            solution[i] = m.grab(i, solution, nums)
            m.add(i, solution)
        return max(solution)
