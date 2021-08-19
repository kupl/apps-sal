class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for (p, s) in cars]
        res = 0
        while len(times) >= 2:
            lead = times.pop()
            if times[-1] > lead:
                res += 1
            else:
                times[-1] = lead
        return res + len(times)
