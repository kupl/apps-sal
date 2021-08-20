class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        lens_s = [math.inf] * len(arr)
        lens_e = [math.inf] * len(arr)
        cs = s = e = 0
        for i in range(len(arr)):
            cs += arr[e]
            while cs >= target:
                if cs == target:
                    lens_e[e] = lens_s[s] = e + 1 - s
                cs -= arr[s]
                s += 1
            e += 1
        forward = [math.inf] * (len(arr) + 1)
        for i in range(1, len(arr)):
            forward[i] = min(lens_e[i - 1], forward[i - 1])
        backward = [math.inf] * (len(arr) + 1)
        for i in reversed(list(range(0, len(arr)))):
            backward[i] = min(lens_s[i], backward[i + 1])
        best = math.inf
        for (f, b) in zip(forward, backward):
            best = min(best, f + b)
        if best == math.inf:
            return -1
        return best
