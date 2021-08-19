class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True

        N = len(nums)
        if N % k:  # 数组的长度不是k的倍数, impossible, 无法分割
            return False
        nums = sorted(nums)
        queue: List[List[int]] = list()

        for index in range(N):
            num = nums[index]
            if len(queue) == 0:
                new_group = [num, 1]    # 初始化[num, size]的数组
                queue.append(new_group)
            else:
                current = queue.pop(0)
                last_num = current[0]
                size = current[1]
                if last_num == num - 1:  # 判断新的num能否放入队列最前面的数组中
                    if size == k - 1:
                        continue        # 加入新的num后的数组满足大小为k，符合条件，移出队列
                    else:
                        size += 1
                        update_group = [num, size]
                        queue.append(update_group)  # 更新[num, size]数组，放回队列
                elif last_num == num:
                    # 新的num无法放入队列最前面的数组中，后序数组也无法放下，创建一个新的数组放入队列
                    # 维护队列最前面的数组为最有可能放入新num的数组
                    new_group = [num, 1]
                    queue.append(current)
                    queue.append(new_group)
                else:  # 新的num无法加入队列，无法继续切分原数组
                    return False
        if len(queue) == 0:  # 符合大小为k的数组全部移出了队列，原数组可以被平均切分
            return True
        else:   # 原数组无法被平均切分成多个大小为k的数组
            return False
