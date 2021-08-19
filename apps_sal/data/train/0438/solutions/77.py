class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        ans = -1
        r = []
        b = [0] * len(arr)
        i = 0
        while i < len(arr):
            v1 = arr[i] > 1 and b[arr[i] - 2]
            v2 = arr[i] < len(arr) and b[arr[i]]
            if v1 and v2:
                h = b[arr[i]]
                t = b[arr[i] - 2]
                b[arr[i]] = 0
                b[arr[i] - 2] = 0
            elif v1:
                h = arr[i]
                t = b[arr[i] - 2]
                b[arr[i] - 2] = 0
            elif v2:
                h = b[arr[i]]
                t = arr[i]
                b[arr[i]] = 0
            else:
                h = arr[i]
                t = h
            b[t - 1] = h
            b[h - 1] = t
            i += 1
            if h - t + 1 == m:
                ans = i
                r.append((t, h))
            elif r:
                while r and (not b[r[-1][0] - 1] == r[-1][1]):
                    r.pop()
                if r:
                    ans = i
        return ans
