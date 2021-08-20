class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        h = defaultdict(int)
        result = -1
        counter = defaultdict(int)
        for i in range(len(arr)):
            n = arr[i] - 1
            l = h[n - 1]
            r = h[n + 1]
            if l > 0 or r > 0:
                newL = l + r + 1
                if l > 0:
                    h[n - l] = newL
                    counter[l] -= 1
                if r > 0:
                    h[n + r] = newL
                    counter[r] -= 1
                h[n] = newL
                counter[newL] += 1
            else:
                h[n] = 1
                counter[1] += 1
            if counter[m] > 0:
                result = i + 1
        return result
