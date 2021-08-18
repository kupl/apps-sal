class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:

        top = defaultdict(lambda: float('inf'))
        bottom = defaultdict(lambda: -1)

        left = defaultdict(lambda: float('inf'))
        right = defaultdict(lambda: -1)

        for row in range(len(targetGrid)):
            for col in range(len(targetGrid[row])):
                color = targetGrid[row][col]

                top[color] = min(top[color], row)
                bottom[color] = max(bottom[color], row)

                left[color] = min(left[color], col)
                right[color] = max(right[color], col)

        edges = defaultdict(list)

        for row in range(len(targetGrid)):
            for col in range(len(targetGrid[row])):
                color = targetGrid[row][col]

                for otherColor in top:
                    if color != otherColor and top[otherColor] <= row <= bottom[otherColor] and left[otherColor] <= col <= right[otherColor]:
                        edges[otherColor].append(color)

        nodestates = [0 for _ in range(61)]

        def dfs(current):
            nodestates[current] = 1

            for neighbor in edges[current]:
                if nodestates[neighbor] == 1:
                    return True
                elif nodestates[neighbor] == 0:
                    dfs(neighbor)

            nodestates[current] = 2

        cycleDetected = False
        for node in top:
            if nodestates[node] == 0:
                if dfs(node):
                    cycleDetected = True
                    break

        return not cycleDetected
