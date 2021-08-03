class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        # res, cur = set(), set()
        # for num in A:
        #     cur = {val | num for val in cur} | {num}
        #     res |= cur
        # return len(res)

        # list
        res = []
        left, right = 0, 0
        for val in A:
            right = len(res)
            res.append(val)
            for i in range(left, right):
                if res[-1] != (res[i] | val):
                    res.append(res[i] | val)
            left = right
        return len(set(res))
