class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        move = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        right = {'N': 'E', 'S': 'W', 'E': 'S', 'W': 'N'}
        left = {'N': 'W', 'S': 'E', 'E': 'N', 'W': 'S'}

        pos = (0, 0)
        dire = 'N'

        for c in instructions:
            if c == 'G':
                x, y = pos
                dx, dy = move[dire]
                pos = (x + dx, y + dy)
            elif c == 'L':
                dire = left[dire]
            else:
                dire = right[dire]

        return pos == (0, 0) or dire != 'N'
