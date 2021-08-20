class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        if n == 0:
            return False
        if arr[start] == 0:
            return True
        queue = [start]
        visited = [False for _ in range(n)]
        while queue:
            index = queue.pop(0)
            visited[index] = True
            right = index + arr[index]
            left = index - arr[index]
            if right < n and (not visited[right]):
                if arr[right] == 0:
                    return True
                queue.append(right)
            if left >= 0 and (not visited[left]):
                if arr[left] == 0:
                    return True
                queue.append(left)
        return False
