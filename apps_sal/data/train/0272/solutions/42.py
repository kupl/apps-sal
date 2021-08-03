class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        self.keys_found = set()
        self.boxes_found = set()
        self.boxes_found.update(initialBoxes)
        n = len(status)
        visited = [0] * n
        for box in initialBoxes:
            self.dfs(box, keys, containedBoxes, visited)

        ans = 0
        for i in range(n):
            if i in self.boxes_found and (i in self.keys_found or status[i] == 1):
                ans += candies[i]
        return ans

    def dfs(self, cur, keys, containedBoxes, visited):
        if visited[cur] == 1:
            return

        visited[cur] = 1
        boxes = containedBoxes[cur]
        self.keys_found.update(keys[cur])
        self.boxes_found.update(boxes)

        for box in boxes:
            self.dfs(box, keys, containedBoxes, visited)
