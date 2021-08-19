class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        if S == 0 and sum(A) == 0:
            return len(A) * (len(A) + 1) // 2

        def atmost(s):
            if s < 0:
                return 0
            sumi = s
            l = 0
            r = 0
            count = 0
            while r < len(A):
                sumi -= A[r]
                while sumi < 0:
                    sumi += A[l]
                    l += 1
                count += r - l + 1
                r += 1
            return count
        return atmost(S) - atmost(S - 1)
