class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True

        N = len(nums)
        if N % k:
            return False
        nums = sorted(nums)
        queue: List[List[int]] = list()

        for index in range(N):
            num = nums[index]
            if len(queue) == 0:
                new_group = [num, 1]
                queue.append(new_group)
            else:
                current = queue.pop(0)
                last_num = current[0]
                size = current[1]
                if last_num == num - 1:
                    if size == k - 1:
                        continue
                    else:
                        size += 1
                        update_group = [num, size]
                        queue.append(update_group)
                elif last_num == num:
                    new_group = [num, 1]
                    queue.append(current)
                    queue.append(new_group)
                else:
                    return False
        if len(queue) == 0:
            return True
        else:
            return False
