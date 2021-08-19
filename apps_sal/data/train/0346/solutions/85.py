class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        count = 0
        dic = defaultdict(int)
#        cum sum
        dic[0] = 1
        ans = 0

        for i in range(1, len(nums) + 1):
            count += nums[i - 1] % 2
            if (count - k) in list(dic.keys()):
                ans += dic[count - k]
            dic[count] += 1
        return ans
