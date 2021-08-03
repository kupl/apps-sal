class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if not arr or len(arr) < k:
            return 0

        summ = [0]
        res = 0
        for p, v in enumerate(arr):
            i = p + 1
            summ.append(summ[p] + v)
            if i - k >= 0:
                if (summ[i] - summ[i - k]) / k >= threshold:
                    res += 1

        return res
