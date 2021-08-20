class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        posToSpeed = {position[i]: speed[i] for i in range(len(position))}
        position.sort()
        leaderTime = (target - position[-1]) / posToSpeed[position[-1]]
        currGroups = 1
        for i in range(len(position) - 2, -1, -1):
            currTime = (target - position[i]) / posToSpeed[position[i]]
            if currTime > leaderTime:
                currGroups += 1
                leaderTime = currTime
        return currGroups
