class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        (cur, res) = (set(), set())
        for num in A:
            cur = {num | j for j in cur}
            cur.add(num)
            res.update(cur)
        return len(res)
