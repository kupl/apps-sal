class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        heapq._heapify_max(arr)
        steps = []
        last = heapq._heappop_max(arr)
        s = last
        c = 1
        while len(arr) > 0:
            v = heapq._heappop_max(arr)
            s += v
            if v != last:
                steps.append([c, last])
                last = v
            c += 1
        steps.append([c, last])
        i = 0
        bestDiff = s - target
        bestValue = steps[0][1]
        while i < len(steps):
            t = int((s - target) / steps[i][0])
            diff = steps[i][0] * t
            if i != len(steps) - 1:
                diff = steps[i][0] * (steps[i][1] - steps[i + 1][1])
            if s - diff > target and i != len(steps) - 1:
                s -= diff
                bestDiff = s - target
                bestValue = steps[i + 1][1]
                i += 1
            elif s - diff == target:
                if i != len(steps) - 1:
                    return steps[i + 1][1]
                else:
                    return steps[i][1] - t
            else:
                diff1 = s - steps[i][0] * t
                diff2 = s - steps[i][0] * (t + 1)
                if bestDiff < abs(diff1 - target):
                    return bestValue
                if abs(diff1 - target) >= abs(diff2 - target):
                    return steps[i][1] - (t + 1)
                else:
                    return steps[i][1] - t
        return bestValue
