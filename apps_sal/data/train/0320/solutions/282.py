class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        count = 0
        nums = [num for num in nums if num]
        if not nums:
            return 0
        while nums:
            flag = False
            new_nums = []
            for num in nums:
                if num % 2:
                    flag = True
                    break
            if flag:
                for num in nums:
                    if num % 2:
                        num = num - 1
                        count += 1
                    if num:
                        new_nums.append(num)
            else:
                for num in nums:
                    new_nums.append(num / 2)
                count += 1
            nums = new_nums
        return count
        

