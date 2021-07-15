class Solution:
    def minOperations(self, A: List[int]) -> int:
        if all(v == 0 for v in A):
            return 0
        odds = 0
        A_next = A.copy()
        for i, v in enumerate(A):
            if v % 2 == 1:
                odds += 1
                A_next[i] = v-1
        if odds > 0:
            return odds + self.minOperations(A_next)
        return 1 + self.minOperations([v//2 for v in A])
        

