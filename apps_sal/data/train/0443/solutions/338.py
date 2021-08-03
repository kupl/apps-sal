class Solution:
    def numTeams(self, rating: List[int]) -> int:
        m_counter = 0
        for index, v1 in enumerate(rating):
            for jdex, v2 in enumerate(rating[index + 1:]):
                if v1 < v2:
                    m_counter = m_counter + len([k for k in rating[jdex + index + 1:] if k > v2])
                else:
                    m_counter = m_counter + len([k for k in rating[jdex + index + 1:] if k < v2])
                print(m_counter)
        return m_counter
