class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def count(d):
            curr = position[0]
            ans = 1
            for i in range(1, len(position)):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans
        (l, r) = (0, position[-1] - position[0])
        while l < r:
            mid = r - (r - l) // 2
            c = count(mid)
            if c >= m:
                l = mid
            else:
                r = mid - 1
        return l
