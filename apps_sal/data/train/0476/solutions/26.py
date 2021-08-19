class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)))
        print(cars)
        times = [(target - p) / s for p, s in cars]

        ans = 0

        while (len(times) > 1):  # that means atleast 2 elements must be there cause we will pop one and then check one for comparing
            lead = times.pop()
            if lead < times[-1]:
                ans += 1
            else:
                times[-1] = lead

        return(ans + len(times))  # remaining car is fleet if it exists
