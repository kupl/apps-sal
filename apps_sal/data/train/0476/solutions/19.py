class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) < 1:
            return 0
        acc = [(position[i], speed[i]) for i in range(len(position))]
        acc = sorted(acc, key=lambda x: x[0])
        
        fleets = 1
        predecessor_arrival = (target - acc[-1][0])/acc[-1][1]
        
        for i in range(len(acc) - 2, -1, -1):
            arrival = (target - acc[i][0])/acc[i][1]
            if arrival > predecessor_arrival:
                fleets += 1
                predecessor_arrival = arrival
        return fleets
        
# position: [10,8,0,5,3] -> [0,3,5,8,10]
# spee:     [2,4,1,1,3]  -> [1,3,1,4,2]

if True:
    print((Solution().carFleet(
        10,
        [0,4,2],
        [2,1,3]))) # 1
# [0,2,4]
# [2,3,1]
# [5,3,6]

# pos[i] + x1*speed[i] == 12
# pos[i+1] + x2*speed[i+1] == 12
# x1 = (12 - pos[i])/speed[i]
# x2 = (12 - pos[i+1])/speed[i+1]

