class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 二分查找
        # 判断若x为最小磁力,能否分隔出m-1个间隔
        def Valid(x):
            ans = 0
            target = position[0]
            for i in range(1, len(position)):
                if position[i] - target >= x:
                    ans += 1
                    target = position[i]
            return ans >= m - 1
        position.sort()
        l, r = min(position[i + 1] - position[i] for i in range(len(position) - 1)), (position[-1] - position[0]) // (m - 1)
        while l <= r:
            mid = l + (r - l) // 2
            # 若最小磁力可以分成m-1个间隔,则可能存在更大值,否则最小磁力值应当更小
            if Valid(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l - 1
