class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, speed) for pos, speed in zip(position, speed)]
        cars.sort()
        
        last_t = -1
        curr_t = 0
        fleets = 0
        
        for pos, speed in reversed(cars):
            curr_t = (target - pos) / speed
            
            if curr_t > last_t:
                fleets += 1
                last_t = curr_t
        
        return fleets
