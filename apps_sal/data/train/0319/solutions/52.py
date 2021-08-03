class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.cache = [0] * 50001
        total = sum(stoneValue)
        first = (total + self.helper(stoneValue, 0)) // 2
        second = total - first
        if first > second:
            return 'Alice'
        elif first < second:
            return 'Bob'
        else:
            return 'Tie'

    def helper(self, stoneValue, index):
        if self.cache[index]:
            return self.cache[index]

        n = len(stoneValue)
        if index == n:
            return 0

        cur = 0
        best = -sys.maxsize
        for i in range(3):
            if index + i >= n:
                break

            cur += stoneValue[index + i]
            best = max(best, cur - self.helper(stoneValue, index + i + 1))

        self.cache[index] = best
        return best
