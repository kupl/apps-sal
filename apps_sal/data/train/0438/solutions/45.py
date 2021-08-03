class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        a, b, s, t = [0] * (len(arr) + 2), [0] * (len(arr) + 1), -1, 0
        for p, i in enumerate(arr, 1):
            j, k = a[i - 1], a[i + 1]
            a[i] = a[i - j] = a[i + k] = j + k + 1
            if a[i] == m:
                t += 1
            if j == m:
                t -= 1
            if k == m:
                t -= 1
            if t:
                s = p
        return s
