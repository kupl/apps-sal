class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        st = set(A)
        lenth = 0
        dq = collections.deque()
        for j in range(1, len(A) - 1):
            for i in range(j):
                if A[i] + A[j] in st:
                    lenth = 3
                    dq.append([3, A[j], A[i] + A[j]])
        while dq:
            sz = len(dq)
            for _ in range(sz):
                s = dq.popleft()
                if s[1] + s[2] in st:
                    (s[0], s[1], s[2]) = (s[0] + 1, s[2], s[1] + s[2])
                    lenth = max(lenth, s[0])
                    dq.append(s)
        return lenth
