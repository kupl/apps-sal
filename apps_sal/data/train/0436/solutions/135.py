class Solution:
    def minDays(self, n: int) -> int:
        if n == 1: return 1
        cnt = 0
        st = set([n])
        while st:
            cnt += 1
            st_temp = set()
            for v in st:
                if v == 1:
                    return cnt
                st_temp.add(v - 1)
                if v % 2 == 0:
                    st_temp.add(v // 2)
                if v % 3 == 0:
                    st_temp.add(v // 3)
            st = st_temp
            # print(len(st_temp))
        return -1

