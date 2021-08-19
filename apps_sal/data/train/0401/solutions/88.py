class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        dic = [0, 0, 0]
        for i in nums:
            if i % 3 == 0:
                dic[0] += i
                if dic[2] != 0:
                    dic[2] += i
                if dic[1] != 0:
                    dic[1] += i
            elif i % 3 == 1:
                (a, b, c) = (dic[0], dic[1], dic[2])
                dic[1] = max(a + i, dic[1])
                if b != 0:
                    dic[2] = max(b + i, dic[2])
                if c != 0:
                    dic[0] = max(c + i, dic[0])
            elif i % 3 == 2:
                (a, b, c) = (dic[0], dic[1], dic[2])
                dic[2] = max(a + i, dic[2])
                if c != 0:
                    dic[1] = max(c + i, dic[1])
                if b != 0:
                    dic[0] = max(b + i, dic[0])
        return dic[0]
