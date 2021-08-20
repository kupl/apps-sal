class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        (result, prev) = (set(), set())
        for num in A:
            temp = set()
            temp.add(num)
            result.add(num)
            for p in prev:
                temp.add(p | num)
                result.add(p | num)
            prev = temp
        return len(result)
