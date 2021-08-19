class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # m表示球的数量
        # 寻找m-1个空隙，来满足距离要求
        def dist_valid(interval, k):
            count, k_count = 0, 0
            for i in interval:
                count += i
                if count >= k:
                    count = 0
                    k_count += 1
                    if k_count >= m - 1:
                        return True
            return False

        interval = []
        sort_pos = sorted(position)
        for i in range(len(sort_pos) - 1):
            interval.append(sort_pos[i + 1] - sort_pos[i])
        left = 1
        right = (max(sort_pos) - min(sort_pos)) // (m - 1)
        while left < right:
            mid = right - (right - left) // 2
            if dist_valid(interval, mid):
                left = mid
            else:
                right = mid - 1
        return left
