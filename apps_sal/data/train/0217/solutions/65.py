class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        res = set()

        last = set()

        for x in A:
            new = {x}

            for y in last:
                new.add(x | y)

            res |= new
            last = new

        return len(res)
