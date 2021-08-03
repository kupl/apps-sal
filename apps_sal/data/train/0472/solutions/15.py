class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        size = len(arr)
        visited = [0] * size

        def trackback(index):
            if arr[index] == 0:
                return True
            if index + arr[index] < size and visited[index + arr[index]] == 0:
                visited[index + arr[index]] = 1
                if trackback(index + arr[index]):
                    return True
            if index - arr[index] > -1 and visited[index - arr[index]] == 0:
                visited[index - arr[index]] = 1
                if trackback(index - arr[index]):
                    return True
            return False
        visited[start] = 1
        return trackback(start)
