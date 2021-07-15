class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # 类似于前缀和 看区间
        # sums 记录从第一个不是0 开始 到当前index的正负情况
        # 如果sums 是负的话，看之前有没有negative 的index
        # 如果有，减去上一个negative 的index， 上一个negative index 到 当前index 整个区间就变成正的了
        # 如果没有，记录当前的index 更新negative
        # 如果sums 是正的话， 直接更新，当前idnex 减去 上一个0 的位置，或者 初始化 -1
        # 如果遇到0，全部初始化 重新计算
        positive_index = - 1
        negative_index = - 1
        sums = 1
        result = 0
        for i in range(len(nums)):
            if sums * nums[i] < 0:
                sums = -1
            elif sums * nums[i] > 0:
                sums = 1
            
            if nums[i] == 0:
                positive_index = i
                negative_index = -1
                sums = 1
            elif sums > 0:
                result = max(result, i - positive_index)
            else:
                if negative_index == -1:
                    negative_index = i
                else:
                    result = max(result, i - negative_index)
                    print(result)
        return result
