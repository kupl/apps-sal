class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        mapping = {0: [1, 0], 1: [0, 1], 2: [-1, 0], 3: [0, -1]}

        direction = 0
        current = [0, 0]

        for instr in instructions:
            if instr == 'L':
                direction -= 1
            elif instr == 'R':
                direction += 1
            elif instr == 'G':
                move = mapping[direction]

                current[0] += move[0]
                current[1] += move[1]

            direction %= 4

        if current == [0, 0] or direction != 0:
            return True
        return False
