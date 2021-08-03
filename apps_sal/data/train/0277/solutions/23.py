class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:

        req = 1
        seen = set()
        ans = 0
        for i, n in enumerate(light, start=1):
            seen.add(n)

            if n == req:
                while req in seen:
                    seen.remove(req)
                    req += 1
            if not seen:
                ans += 1

        return ans
