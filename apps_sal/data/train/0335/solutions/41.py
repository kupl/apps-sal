class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        m_sum = sum(rods) // 2
        m = [[-2 for i in range(m_sum + 1)] for j in range(len(rods))]

        def dfs(i, s1, s2):
            if s1 > m_sum or s2 > m_sum:
                return -1
            if i == len(rods):
                return s1 if s1 == s2 else -1
            if m[i][abs(s1 - s2)] == -2:
                m[i][abs(s1 - s2)] = max(dfs(i + 1, s1 + rods[i], s2), dfs(i + 1, s1, s2 + rods[i]), dfs(i + 1, s1, s2)) - max(s1, s2)
            return m[i][abs(s1 - s2)] + (max(s1, s2) if m[i][abs(s1 - s2)] != -1 else 0)
        return max(0, dfs(0, 0, 0))
