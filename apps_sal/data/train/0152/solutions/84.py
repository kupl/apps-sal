class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        ans = top = (position[-1] - position[0]) // (m - 1)
        down = 0
        while ans != down:
            if self._test(position, ans, m - 1):
                down = ans
            else:
                top = ans
            ans = (top + down) // 2
        return down

    def _test(self, position, force, m):
        i = 0
        while i < len(position) and m > 0:
            if len(position) - 1 - i < m:
                return False
            total = 0
            while total < force:
                i += 1
                if i >= len(position):
                    break
                total += position[i] - position[i - 1]
            if total >= force:
                m -= 1
        if m == 0:
            return True
        return False
