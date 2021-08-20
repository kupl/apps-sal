class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def valid_distance(d):
            (cur, idx, total) = (0, 1, 1)
            while idx < len(position) and total < m:
                if position[idx] - position[cur] >= d:
                    total += 1
                    cur = idx
                idx += 1
            return total == m
        position.sort()
        (s, e) = (0, position[-1] - position[0] + 1)
        while s < e:
            mid = s + (e - s) // 2
            if valid_distance(mid):
                s = mid + 1
            else:
                e = mid
        return s - 1
