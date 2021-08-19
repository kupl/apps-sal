class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ind = sorted(range(len(position)), key=lambda x: position[x])
        print(ind)
        r = len(speed) - 1
        fleet_num = 0
        while r >= 0:
            time = (target - position[ind[r]]) / speed[ind[r]]
            position[ind[r]] = target
            r = r - 1
            while r >= 0 and position[ind[r]] + speed[ind[r]] * time >= target:
                position[ind[r]] = target
                r = r - 1
            fleet_num += 1
            for i in range(r + 1, -1):
                position[ind[i]] = min(position[ind[i]] + time * speed[ind[i]], position[ind[i + 1]])
        return fleet_num
