class Solution:

    def minOperations(self, nums: List[int]) -> int:
        mem = {}
        ans = [[0 for i in range(len(nums))] for j in range(2)]
        for (i, num) in enumerate(nums):
            times = [0, 0]
            _num = num
            while _num != 0:
                if _num in mem:
                    times[0] += mem[_num][0]
                    times[1] += mem[_num][1]
                    break
                if _num % 2 == 1:
                    _num -= 1
                    times[0] += 1
                else:
                    _num /= 2
                    times[1] += 1
            mem[num] = times
            ans[0][i] = times[0]
            ans[1][i] = times[1]
        print(ans)
        return sum(ans[0]) + max(ans[1])
