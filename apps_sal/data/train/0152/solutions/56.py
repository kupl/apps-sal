class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 最大间隙使用二分法查找
        # 检查最大间隙的合理性
        # 从一堆间隙中，寻找连续长度为dist的m个间隙
        interval = []
        sort_pos = sorted(position)
        for i in range(len(sort_pos)-1):
            interval.append(sort_pos[i+1]-sort_pos[i])
        
        def is_valid(dist,interval):
            ball = 1
            count = 0
            for i in interval:
                count += i
                if count>=dist:
                    ball += 1
                    count = 0
            if ball>=m:
                return True
            return False
        
        left = 1
        right = sum(interval)//(m-1)
        # 如果最优值停在right上，那么这个循环永远不能结束
        while left<right:
            mid = right - (right-left)//2
            if is_valid(mid,interval):
                left = mid
            else:
                right = mid - 1
        return left
            

