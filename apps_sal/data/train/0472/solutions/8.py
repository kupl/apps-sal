class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        v = set()
        q = [start]
        while q:
            i = q.pop()
            v.add(i)
            if arr[i] == 0:
                return True
            for idx in [(i + arr[i]), i - arr[i]]:
                if 0 <= idx < len(arr) and idx not in v:
                    q.append(idx)
        return False
