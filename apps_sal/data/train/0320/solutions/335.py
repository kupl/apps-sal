class Solution:
    def minOperations(self, A: List[int]) -> int:
        if all(v == 0 for v in A):
            return 0
        curr = 0
        A_next = A.copy()
        changed = False
        for i, v in enumerate(A):
            if v % 2 == 1:
                changed = True
                curr += 1
                A_next[i] = v-1
        if not changed:
            return 1 + self.minOperations([v//2 for v in A])
        else:
            return curr + self.minOperations(A_next)

