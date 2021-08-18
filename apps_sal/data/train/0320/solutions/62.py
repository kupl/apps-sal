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
