class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        st = []
        ret = 0
        for (i, s) in enumerate(A):
            while len(st) > 0 and st[-1][0] < s:
                (s_j, j) = st.pop()
                ret = max(ret, s + s_j - abs(i - j))
            if len(st) > 0:
                ret = max(ret, s + st[-1][0] - abs(st[-1][1] - i))
            st.append((s, i))
        return ret
