class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev_s = [None for _ in seats]
        next_s = [None for _ in seats]
        last_1 = -float('INF')
        next_1 = float('INF')
        for i in range(len(seats)):
            if seats[i] == 1:
                last_1 = i
            else:
                prev_s[i] = last_1
        
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                next_1 = i
            else:
                next_s[i] = next_1
        
        print(prev_s, next_s)
        closest_max = -1
        for i in range(len(seats)):
            if prev_s[i] != None and next_s[i] != None:
                print(prev_s[i], next_s[i])
                closest_max = max(closest_max, min(i - prev_s[i], next_s[i] - i))
        return closest_max
