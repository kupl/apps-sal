class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)

        l = 1
        r = position[-1] - position[0]

        def check(diff, m):
            ctr = 1
            prev = 0

            for i in range(1, len(position)):
                if ctr == m:
                    return True
                if position[i] - position[prev] >= diff:
                    ctr += 1
                    prev = i

            if ctr == m:
                return True
            return False

        val = -10**10

        while l <= r:
            mid = (l + r) // 2

            if check(mid, m):
                val = max(val, mid)
                l = mid + 1
            else:
                r = mid - 1

        return val
