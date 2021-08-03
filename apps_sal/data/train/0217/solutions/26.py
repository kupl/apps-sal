class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        # Brute force with set, with list we can use if in list conditional statement
        # Slow & bad....

        #        rset = set()
        #        for i in range(len(A)):
        #            for j in range(i+1, len(A)+1):
        #                res = 0
        #                for k in range(i, j):
        #                    res |= A[k]
        #                rset.add(res)
        #        return len(rset)

        #        A cleaner code
        #        Assume B[i][j] = A[i] | A[i+1] | ... | A[j]
        #        Hash set cur stores all wise B[0][i], B[1][i], B[2][i], B[i][i].

        #        When we handle the A[i+1], we want to update cur
        #        So we need operate bitwise OR on all elements in cur.
        #        Also we need to add A[i+1] to cur.

        #        In each turn, we add all elements in cur to res.
        # This method is better since it preserves the results of previous operation and make them useful
        res, cur = set(), set()

        for i in A:
            cur = {i | j for j in cur} | {i}
            res |= cur

        return len(res)
