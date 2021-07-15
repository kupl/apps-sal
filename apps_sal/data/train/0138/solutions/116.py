class Solution:
    def isEven(self, num):
        return num % 2 == 0
    
    def getMaxLen(self, nums: List[int]) -> int:
        return max(self.getMaxLenOne(nums), self.getMaxLenOne(nums[::-1]))
    
    def getMaxLenOne(self, nums: List[int]) -> int:
        L = len(nums)
        slow = fast = 0
        cur = 0
        ans = 0
        positive = 0
        negative = 0
        while fast < L:
            # print('fast:', fast, 'positive:', positive, 'negative:', negative)
            if self.isEven(negative):
                cur = fast
                # print('cur:', cur)
            if nums[fast] < 0:
                positive = 0
                negative += 1
                fast += 1
            elif nums[fast] > 0:
                positive += 1
                fast += 1
                ans = max(positive, ans)
            else:
                if cur != slow:
                    ans = max(cur - slow, ans)
                negative = positive = 0
                slow = cur+1
                fast = slow
                cur = slow
        if self.isEven(negative):
            cur = fast
        return max(ans, cur-slow)

