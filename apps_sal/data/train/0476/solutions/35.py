class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by starting position
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for p, s, in cars]
        # count from back
        most = 0
        count = 0
        for i in range(len(times)-1 ,-1, -1):
            if times[i] > most:
                most = times[i]
                count += 1
                
        return count
