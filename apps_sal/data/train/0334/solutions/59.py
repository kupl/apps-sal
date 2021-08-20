class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        st = []
        ans = 0
        for i in range(len(s)):
            if len(st) == 0:
                st.append(i)
            elif s[i] == s[st[-1]]:
                if cost[st[-1]] < cost[i]:
                    ans += cost[st[-1]]
                    st.pop()
                    st.append(i)
                else:
                    ans += cost[i]
            else:
                st.append(i)
        return ans
