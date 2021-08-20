class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        N = len(A)
        lefts = []
        st = []
        for (i, num) in enumerate(A):
            cnt = 1
            while st and st[-1][0] > num:
                (prev_num, prev_cnt) = st.pop()
                cnt += prev_cnt
            st.append([num, cnt])
            lefts.append(cnt)
        rights = []
        st = []
        for (i, num) in reversed(list(enumerate(A))):
            cnt = 1
            while st and st[-1][0] >= num:
                (prev_num, prev_cnt) = st.pop()
                cnt += prev_cnt
            st.append([num, cnt])
            rights.append(cnt)
        ans = 0
        for (lc, num, rc) in zip(lefts, A, rights[::-1]):
            ans += lc * num * rc
        return ans % (10 ** 9 + 7)
