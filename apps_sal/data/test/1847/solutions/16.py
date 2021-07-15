from collections import deque, defaultdict


class Solution:

    def solve(self):
        kpos = input().split()
        kpos = [int(x) for x in kpos]
        startK = [kpos[0], kpos[1]]
        endK = [kpos[2], kpos[3]]
        N = int(input())

        intervals_dict = defaultdict(list)
        for _ in range(N):
            allowed = input().split()
            allowed = [int(x) for x in allowed]
            row, start, end = allowed
            intervals_dict[row].append([start, end])

        # merge intervals
        for row in intervals_dict:
            intervals = intervals_dict[row]
            intervals.sort()
            final_merged = []

            last_start, last_end = intervals[0]
            for interval in intervals[1:]:
                start, end = interval
                if start <= last_end:
                    last_end = end
                    continue
                final_merged.append([last_start, last_end])
                last_start = start
                last_end = end

            final_merged.append([last_start, last_end])
            last_start = start
            intervals_dict[row] = final_merged

        # BFS
        queue = deque([startK])
        moves = 0
        seen = set((startK[0], startK[1]))
        directions = [(i, j) for i in [1, 0, -1]
                      for j in [1, 0, -1] if not(i == j == 0)]

        def get_intervals(intervals_dict):
            for intervals in intervals_dict:
                yield intervals

        while queue:
            moves += 1
            for i in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    row, col = x + dx, y + dy

                    if row in intervals_dict and (row, col) not in seen:
                        valid = False
                        for interval in intervals_dict[row]:
                            start_int, end_int = interval
                            if start_int <= col <= end_int:
                                valid = True
                                break
                        if valid:
                            intervals_dict[row][0][0] <= col <= intervals_dict[row][0][1]
                            seen.add((row, col))
                            if (row, col) == (endK[0], endK[1]):
                                return moves
                            queue.append((row, col))

        return -1


soln = Solution()
print(soln.solve())


