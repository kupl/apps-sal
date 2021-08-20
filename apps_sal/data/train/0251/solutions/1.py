class Solution:

    def clumsy(self, N: int) -> int:
        all_nums = [i for i in range(N, 0, -1)]
        prio_nums = []
        for i in range(0, len(all_nums) - 3, 4):
            prio_nums.append(all_nums[i] * all_nums[i + 1] // all_nums[i + 2])
            prio_nums.append(all_nums[i + 3])
        if N % 4 == 3:
            prio_nums.append(all_nums[-3] * all_nums[-2] // all_nums[-1])
        elif N % 4 == 2:
            prio_nums.append(all_nums[-2] * all_nums[-1])
        elif N % 4 == 1:
            prio_nums.append(all_nums[-1])
        total = prio_nums[0]
        print(prio_nums)
        for i in range(1, len(prio_nums)):
            if i % 2 != 0:
                total = total + prio_nums[i]
            else:
                total = total - prio_nums[i]
        return total
