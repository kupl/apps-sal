class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def check(space):
            count = start = 0
            for i in range(1, len(position)):
                if position[i] - position[start] >= space:
                    count += 1
                    start = i
            return count >= m - 1

        def find_space(lo, hi):
            while lo < hi:
                mid = int((lo / 2) + (hi / 2))
                if check(mid) and not check(mid + 1):
                    return mid
                if check(mid):
                    lo = max(mid, lo + 1)
                else:
                    hi = mid
            hi -= 1
            while check(hi):
                hi += 1
            return hi - 1

        position.sort()
        return find_space(1, position[-1] - position[0])
