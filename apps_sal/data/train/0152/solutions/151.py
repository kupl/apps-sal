class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position = sorted(position)

        def count(d, position):
            (m_num, cur) = (1, position[0])
            for p in position:
                if p - cur >= d:
                    m_num += 1
                    cur = p
            return m_num
        l = 0
        r = position[-1] - position[0]
        while l < r:
            mid = l + (r - l) // 2
            m_num = count(mid + 1, position)
            if m_num < m:
                r = mid
            else:
                l = mid + 1
        return l
