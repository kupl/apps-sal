class Solution:
    def minOperations(self, nums: List[int]) -> int:
        multi_max = 0
        answer = 0
        for num in nums:
            cur_multi = 0
            while(num):
                if num % 2 == 1:
                    answer += 1
                    num -= 1
                else:
                    cur_multi += 1
                    num //= 2
            multi_max = max(multi_max, cur_multi)
        return answer + multi_max
        # answer = 0
        # max_num = 0
        # for num in nums:
        #     small = int(math.log(num, 2))
        #     max_num = max(small, max_num)
        #     answer += num - 2**small + 1
        # print(max_num)
        # return answer + max_num
