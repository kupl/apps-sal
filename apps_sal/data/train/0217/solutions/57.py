class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        res, curr = set(), set()
        for a in A:
            temp = {a}
            for b in curr:
                temp.add(a | b)
            curr = temp
            for num in curr:
                res.add(num)
        return len(res)
