class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        s = set()
        global_set = set()
        ans = 0
        for v in A:
            s.add(v)
            s = {x | v for x in s}
            global_set |= s
        return len(global_set)
