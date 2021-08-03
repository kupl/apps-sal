class Solution:
    def isValid(self, S: str) -> bool:
        st = []
        for i, s in enumerate(S):
            st.append(s)
            while st[-3:] == ['a', 'b', 'c']:
                st = st[:-3]
        return len(st) == 0
