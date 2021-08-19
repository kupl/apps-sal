class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        self.res = set()

        def helper(idx):
            if idx < 0:
                return set()
            if idx == 0:
                self.res |= {A[idx]}
                return {A[idx]}
            val = {A[idx]} | {x | A[idx] for x in helper(idx - 1)}
            self.res |= val
            return val
        helper(len(A) - 1)
        return len(self.res)
