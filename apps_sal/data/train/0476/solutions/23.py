class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0
        time_required = []
        for i in range(len(position)):
            time_required.append((target - position[i]) / speed[i])
        time_required = [x for (_, x) in sorted(zip(position, time_required), reverse=True)]
        print(time_required)
        count = 1
        previous_time = time_required[0]
        for i in range(1, len(time_required)):
            if time_required[i] > previous_time:
                count += 1
                previous_time = time_required[i]
        return count
