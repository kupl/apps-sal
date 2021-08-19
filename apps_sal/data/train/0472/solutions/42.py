class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        q = [start]
        while q:
            q = [i for x in q for i in (x - arr[x], x + arr[x]) if 0 <= i < len(arr) and i not in visited]
            for i in q:
                if arr[i] == 0:
                    return True
                visited.add(i)
        return False
