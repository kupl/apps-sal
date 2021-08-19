class Solution:

    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        start = sum((val << i * n + j for (i, row) in enumerate(mat) for (j, val) in enumerate(row)))
        queue = collections.deque([(start, 0)])
        seen = {start}
        dirs = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]
        while queue:
            (current, d) = queue.popleft()
            if current == 0:
                return d
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    next_state = current
                    for dir_ in dirs:
                        new_i = i + dir_[0]
                        new_j = j + dir_[1]
                        if new_i >= 0 and new_i < len(mat) and (new_j >= 0) and (new_j < len(mat[0])):
                            next_state ^= 1 << new_i * n + new_j
                    if next_state not in seen:
                        seen.add(next_state)
                        queue.append((next_state, d + 1))
        return -1
