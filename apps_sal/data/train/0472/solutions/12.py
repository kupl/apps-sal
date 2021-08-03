class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        size = len(arr)
        visited = [[0] * 2 for _ in range(size)]

        def trackback(index):
            if arr[index] == 0:
                return True
            if index + arr[index] < size and visited[index][1] == 0:
                visited[index][1] = 1
                if trackback(index + arr[index]):
                    return True
            if index - arr[index] > -1 and visited[index][0] == 0:
                visited[index][0] = 1
                if trackback(index - arr[index]):
                    return True
            return False
        return trackback(start)
