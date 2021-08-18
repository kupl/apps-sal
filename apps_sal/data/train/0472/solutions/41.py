class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        if not arr:
            return False
        if arr[start] == 0:
            return True
        queue = [start]
        n = len(arr)
        visited = [False for _ in range(n)]

        while queue:
            index = queue.pop(0)
            visited[index] = True
            newIndices = [index - arr[index], index + arr[index]]

            for i in newIndices:
                if i >= 0 and i < n and not visited[i]:
                    queue.append(i)
                    if arr[i] == 0:
                        return True
        return False
