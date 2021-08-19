class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        sat.sort()
        split = 0
        while split < len(sat) and sat[split] < 0:
            split += 1
        if split == len(sat):
            return 0
        cur_sum, i, unit = 0, 1, 0
        for x in sat[split:]:
            cur_sum += (i * x)
            unit += x
            i += 1
        self.max = cur_sum
        #print(split, cur_sum, unit)
        for i in range(split - 1, -1, -1):
            r, diff, psum = 1, 0, cur_sum
            for j in range(i, split):
                diff += (r * sat[j])
                r += 1
                psum += unit
            psum += diff
            if psum > self.max:
                self.max = psum
        return self.max
