class Solution:

    def isRobotBounded(self, instructions: str) -> bool:

        def is_infinite_loop(command):
            direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            d_index = 0
            (x, y) = (0, 0)
            for move in command:
                if move == 'G':
                    x += direction[d_index][0]
                    y += direction[d_index][1]
                elif move == 'R':
                    d_index = (d_index + 1) % 4
                elif move == 'L':
                    d_index = (d_index + 3) % 4
            if x == y == 0:
                return True
            if (x != 0 or y != 0) and d_index != 0:
                return True
            return False
        return is_infinite_loop(instructions)
