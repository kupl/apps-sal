class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - p) / s for p, s in sorted(zip(position, speed), key=lambda x: x[0])]
        fleets = 0
        last_arrive = 0
        for t in time[::-1]:
            if t > last_arrive:
                last_arrive = t
                fleets += 1
        return fleets
