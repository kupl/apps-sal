class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cumsum = [0] * (n + 1)
        for i in range(n):
            cumsum[i + 1] = cumsum[i] + nums[i]
        d = {0: 0}
        temp = []
        for i in range(n):
            if cumsum[i + 1] - target in d:
                temp.append((d[cumsum[i + 1] - target], i + 1))
            d[cumsum[i + 1]] = i + 1
        l = sorted(temp, key=lambda x: (x[0], x[1]))
        cur_s = -1
        cur_e = -1
        total = 0
        for (s, e) in l:
            if s >= cur_e:
                total += 1
                cur_s = s
                cur_e = e
            elif e < cur_e:
                cur_s = s
                cur_e = e
        return total
