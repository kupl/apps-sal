class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) < 1:
            return 0
        acc = [(position[i], speed[i]) for i in range(len(position))]
        acc = sorted(acc, key=lambda x: x[0])
        fleets = 1
        predecessor_arrival = (target - acc[-1][0]) / acc[-1][1]
        for i in range(len(acc) - 2, -1, -1):
            arrival = (target - acc[i][0]) / acc[i][1]
            if arrival > predecessor_arrival:
                fleets += 1
                predecessor_arrival = arrival
        return fleets


if True:
    print(Solution().carFleet(10, [0, 4, 2], [2, 1, 3]))
