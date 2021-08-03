class Solution:
    def racecar(self, target: int) -> int:
        if target == 0:
            return 1
        self.ans = 0
        self.bfsHelper(target)
        return self.ans

    def bfsHelper(self, target):
        queue = []
        queue.append((0, 1))
        visited = set()
        key = 'pos_' + str(0) + 'speed_' + str(1)
        visited.add(key)

        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                curPos = queue[0][0]
                curSpeed = queue[0][1]
                queue.pop(0)
                if curPos == target:
                    return self.ans

                newPos = curPos + curSpeed
                newSpeed = curSpeed * 2
                key = 'pos_' + str(newPos) + 'speed_' + str(newSpeed)
                if key not in visited and newPos > 0 and newPos < 2 * target:
                    visited.add(key)
                    queue.append((newPos, newSpeed))

                newPos = curPos
                newSpeed = -1 if curSpeed > 0 else 1
                key = 'pos_' + str(newPos) + 'speed_' + str(newSpeed)
                if key not in visited and newPos > 0 and newPos < 2 * target:
                    visited.add(key)
                    queue.append((newPos, newSpeed))

            self.ans += 1

        self.ans = -1
