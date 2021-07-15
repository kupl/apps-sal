class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        import bisect
        # dp存储所有潜在的当前状态（每次dp都是遍历arr1时前一个位置的状态）
        # 这里的状态是一个键值对，key代表当前位置的数字，
        # 可以是arr1里面的，也可以是arr2里面用来替换的
        # value就是我们需要操作的次数
        dp = {-1: 0}
        arr2.sort()
        for i in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for key in dp:
                if i > key:
                    tmp[i] = min(tmp[i], dp[key])
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]], dp[key] + 1)
            dp = tmp
        return min(dp.values()) if dp else -1

