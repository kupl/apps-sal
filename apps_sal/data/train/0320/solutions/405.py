class Solution:
    def minOperations(self, nums: List[int]) -> int:
        odds, even = [], []
        for i in nums:
            if i & 1:
                odds.append(i)
            elif i != 0:
                even.append(i)

        count = 0
        while odds or even:
            if odds:
                i = odds.pop()
                if i - 1 != 0:
                    even.append(i - 1)
            else:
                new_even = []
                for i in even:
                    i //= 2
                    if i & 1:
                        odds.append(i)
                    else:
                        new_even.append(i)
                even = new_even
            count += 1
        return count
