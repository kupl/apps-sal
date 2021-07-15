class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        lists = [[]]
        negative = [[]]
        index = 0
        for num in nums:
            if num == 0:
                index = 0
                negative.append([])
                lists.append([])
            else:
                if num < 0:
                    negative[-1].append(index)
                lists[-1].append(num)
                index += 1

        max_len = 0
        for l, neg in zip(lists, negative):
            if len(neg) % 2 == 1:
                dist = min(neg[0] + 1, len(l) - neg[-1])
            else:
                dist = 0
            max_len = max(len(l) - dist, max_len)
        
        return max_len

