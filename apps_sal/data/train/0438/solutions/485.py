from bisect import bisect_left


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        res = -2

        groups = []
        n = len(arr)

        m_cnt = 0
        for step, x in enumerate(arr):
            k = groups
            if not groups:
                groups.append([x, x])
                if m == 1:
                    m_cnt += 1
            else:
                gn = len(groups)
                left = x
                right = x
                idx = bisect_left(groups, [x, x])

                if idx < gn:
                    if groups[idx][0] == x + 1:
                        right = groups[idx][1]
                        if groups[idx][1] - groups[idx][0] + 1 == m:
                            m_cnt -= 1
                        groups.pop(idx)

                if idx - 1 >= 0:
                    if groups[idx - 1][1] == x - 1:
                        left = groups[idx - 1][0]
                        if groups[idx - 1][1] - groups[idx - 1][0] + 1 == m:
                            m_cnt -= 1
                        groups.pop(idx - 1)
                        idx -= 1

                groups.insert(idx, [left, right])
                if right - left + 1 == m:
                    m_cnt += 1

            if m_cnt:
                res = step
        return res + 1
