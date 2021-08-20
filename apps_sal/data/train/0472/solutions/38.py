from functools import lru_cache


class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:

        def dfs(idx, visited):
            if arr[idx] == 0:
                return True
            left_idx = idx - arr[idx]
            if left_idx >= 0 and left_idx not in visited:
                visited.add(left_idx)
                res = dfs(left_idx, visited)
                if res:
                    return True
            right_idx = idx + arr[idx]
            if right_idx < len(arr) and right_idx not in visited:
                visited.add(right_idx)
                res = dfs(right_idx, visited)
                if res:
                    return True
            return False
        return dfs(start, set([start]))
