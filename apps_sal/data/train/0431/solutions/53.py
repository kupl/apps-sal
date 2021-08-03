class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # 자존감이 낮아지면 힘들다...
        # 내가 노력한 양에 비해 남들의 평가가 낮게 돌아오는것 같기에
        # 이것또한 내가 생각하는 기준!

        # when i see this is minimum on num on left side
        # i can count the number
        # cnt = 1
        # while st and st[-1][0] > curr_num:
        #     pop and increment
        # what happend for increase case? then this case count only once when it used by itself
        N = len(A)
        lefts = []
        st = []
        for i, num in enumerate(A):
            cnt = 1
            while st and st[-1][0] > num:
                prev_num, prev_cnt = st.pop()
                cnt += prev_cnt
            st.append([num, cnt])
            lefts.append(cnt)
        rights = []
        st = []
        for i, num in reversed(list(enumerate(A))):
            cnt = 1
            while st and st[-1][0] >= num:
                prev_num, prev_cnt = st.pop()
                cnt += prev_cnt
            st.append([num, cnt])
            rights.append(cnt)

        ans = 0
        for lc, num, rc in zip(lefts, A, rights[::-1]):
            ans += lc * num * rc
        return ans % (10**9 + 7)
