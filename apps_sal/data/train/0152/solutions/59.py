class Solution:
    def maxDistance(self, positions: List[int], m: int) -> int:

        positions.sort()

        def possible(positions, m, v):

            cur = 0
            for i in range(1, len(positions)):

                if positions[i] - positions[cur] >= v:
                    m -= 1
                    cur = i
                    if m == 1:
                        return True

            return m <= 1

        left, right = 1, positions[-1] - positions[0]

        ans = 0
        while left <= right:

            v = (left + right) // 2
            if possible(positions, m, v):
                ans = v
                left = v + 1
            else:
                right = v - 1

        return ans
