class Solution:
    def racecar(self, target: int) -> int:
        been = set()
        steps = 0
        queue = {(target, 1)}
        while queue:
            print(len(queue))
            newQueue = set()
            for pos, speed in queue:
                if pos == 0: return steps
                been.add((pos, speed))
                nextStatus = (abs(pos - speed), -speed * 2 if speed > pos else speed * 2)
                if nextStatus[0] < target * 2 and nextStatus not in been:
                    newQueue.add(nextStatus)
                nextStatus = (pos, -1 if speed > 0 else 1)
                if nextStatus[0] < target * 2 and nextStatus not in been:
                    newQueue.add(nextStatus)
            steps += 1
            queue = newQueue
