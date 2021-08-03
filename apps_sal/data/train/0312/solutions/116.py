class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        ans = 1 if A[0] >= K else sys.maxsize

        for i in range(1, len(A)):
            A[i] += A[i - 1]
            if A[i] >= K:
                ans = min(ans, i + 1)

        st = [(A[0], 0)]
        for i in range(1, len(A)):
            while len(st) and A[i] - st[0][0] >= K:
                ans = min(ans, i - st[0][1])
                st.pop(0)

            while len(st) and A[i] <= st[-1][0]:
                st.pop()

            st.append((A[i], i))

        return ans if ans != sys.maxsize else -1
