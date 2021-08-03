class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(d):
            i = 0
            j = 1
            for _ in range(m - 1):
                while j < len(position) and position[j] - position[i] < d:
                    j += 1
                if j >= len(position):
                    return False
                i = j
                j = j + 1
            return True
        a = 1
        b = position[-1] - position[0]
        ans = 0
        while a <= b:
            c = (a + b) // 2
            if check(c):
                ans = c
                a = c + 1
            else:
                b = c - 1
        return ans
