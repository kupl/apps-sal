class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        st = set()
        for s in range(1, 1 + len(text) // 2):
            for start in range(len(text)):
                l = text[start:start+s]
                r = text[start+s:start+s+s]
                if l == r and (l+r) not in st and len(l) != 0:
                    st.add(l+r)
        return len(st)
