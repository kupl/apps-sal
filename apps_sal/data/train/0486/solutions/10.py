class Solution:
    def queryString(self, S: str, N: int) -> bool:
        st = set()

        for size in range(1, len(S) + 1):
            for i in range(len(S) - size + 1):
                st.add(S[i:i + size])

        for i in range(1, N + 1):
            if not bin(i)[2:] in st:

                return False

        return True
