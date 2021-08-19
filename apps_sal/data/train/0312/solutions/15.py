class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        sm = 0
        pref = []
        mn = sys.maxsize
        for i in range(len(A)):
            pref.append(A[i] + sm)
            sm += A[i]
        st = [(0, -1)]
        for i in range(len(A)):
            while len(st) and pref[i] < st[-1][0]:
                st.pop()
            while len(st) and pref[i] - st[0][0] >= K:
                mn = min(mn, i - st[0][1])
                st.pop(0)
            st.append([pref[i], i])
        return mn if mn != sys.maxsize else -1
