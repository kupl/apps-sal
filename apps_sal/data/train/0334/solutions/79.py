class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        st = []
        st.append((s[0], 0))
        res = 0
        n = len(s)
        for i in range(1, n):
            if st[-1][0] == s[i]:
                x = st[-1][1]
                if cost[x] >= cost[i]:
                    res += cost[i]
                else:
                    res += cost[x]
                    st.pop()
                    st.append((s[i], i))
            else:
                st.append((s[i], i))
        return res
