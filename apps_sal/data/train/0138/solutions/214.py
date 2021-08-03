class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dct = {0: -1}

        count = 0
        res = 0
        for i, num in enumerate(nums):
            if num < 0:
                count += 1
                # print(num,count,i)
                dct[count] = i

            elif num == 0:
                dct = {0: i}
                count = 0
            if count % 2 == 0:
                res = max(res, i - dct[0])

            else:
                t1 = i - dct[1]
                t2 = 0
                if num < 0:
                    t2 = i - 1 - dct[0]
                res = max(res, max(t1, t2))
            # print(dct,res)
        return res
