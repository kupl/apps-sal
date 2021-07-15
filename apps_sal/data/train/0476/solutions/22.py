class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - pos) / s for pos, s in sorted(zip(position, speed))]
        cur = ans = 0
        for time in times[::-1]:
            if time > cur:
                ans += 1
                cur = time
        return ans
        
    # start a new fleet when cur car's time to target is longer than the leader car of the cur fleet (i.e. cur car can't catch up with last fleet)
    # need to sort cars by position and start looping from the car closest to target becasue 'a car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed'. If we have cars A, B, C. time for A to reach target is shorter than B, then C. If we don't go from C to A, we don't know if there are three fleets or one. Going from C to A tells us it's one  

