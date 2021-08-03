class Solution:
    def minDays(self, n: int) -> int:
        frontier = deque()
        visited = dict()
        visited[n] = 0
        frontier.append(n)

        while frontier:
            curr = frontier.popleft()

            if curr == 0:
                return visited[curr]

            neighbors = [curr - 1]

            if curr % 2 == 0:
                neighbors.append(curr // 2)

            if curr % 3 == 0:
                neighbors.append(curr // 3)

            for nbr in neighbors:
                if nbr not in visited:
                    visited[nbr] = visited[curr] + 1
                    frontier.append(nbr)
        return -1
