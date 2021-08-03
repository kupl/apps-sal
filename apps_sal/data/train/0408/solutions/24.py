class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        vals = sorted(arr)
        l = len(vals)

        diff = float('inf')
        num = -1
        m = vals[-1]
        i = 0
        prev_sum = 0
        for n in range(m + 1):
            if n > target:
                break

            while n > vals[i]:
                prev_sum += vals[i]
                i += 1

            total = (n * (l - i)) + prev_sum
            new_diff = abs(target - total)
            if new_diff < diff:
                diff = new_diff
                num = n

        return num
