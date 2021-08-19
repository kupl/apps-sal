class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = 0
        n = len(light)

        # Actual turned on light (positive)
        # Required turned on light (negative)
        counter = collections.Counter()
        for i in range(n):
            counter[light[i]] += 1
            if counter[light[i]] == 0:
                counter.pop(light[i])

            counter[i + 1] -= 1
            if counter[i + 1] == 0:
                counter.pop(i + 1)

            if not counter:
                res += 1
        return res
