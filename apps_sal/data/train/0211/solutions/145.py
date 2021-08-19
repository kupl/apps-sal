class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[0] == s[1]:
                return 1
            return 2
        ans = 0
        for i in range(2 ** (len(s) - 1)):
            ss = format(i, '0' + str(len(s) - 1) + 'b') + '1'
            st = set()
            count = 0
            prev = 0
            for j in range(len(ss)):
                lth = len(st)
                if ss[j] == '1':
                    st.add(s[prev:j + 1])
                    if len(st) == lth:
                        break
                    prev = j + 1
                    count += 1
            ans = max(ans, count)
        return ans
