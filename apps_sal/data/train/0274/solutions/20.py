class Solution:
    def longestSubarray(self, A, limit):
        M = collections.deque()
        m = collections.deque()
        i = 0
        for a in A:
            while M and a > M[-1]:
                M.pop()
            while m and a < m[-1]:
                m.pop()
            M.append(a)
            m.append(a)
            if M[0] - m[0] > limit:
                if M[0] == A[i]:
                    M.popleft()
                if m[0] == A[i]:
                    m.popleft()
                i += 1
        return len(A) - i
