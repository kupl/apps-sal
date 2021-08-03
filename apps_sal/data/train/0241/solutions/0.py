class Solution:
    def move(self, pos, direction):
        x, y = pos
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x -= 1
        return (x, y)

    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0  # 0 for north, 1 for east, 2 for south, 3 for west
        pos = (0, 0)
        for i in instructions:
            if i == 'G':
                pos = self.move(pos, direction)
            elif i == 'L':
                direction = (direction - 1) % 4
            elif i == 'R':
                direction = (direction + 1) % 4
        if pos == (0, 0) or direction != 0:
            return True
        else:
            return False
