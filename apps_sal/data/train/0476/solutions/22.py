class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - pos) / s for pos, s in sorted(zip(position, speed))]
        cur = ans = 0
        for time in times[::-1]:
            if time > cur:
                ans += 1
                cur = time
        return ans
