class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        d = dict()
        counter = collections.Counter()
        ans = -1
        for i, num in enumerate(arr, 1):
            left = d.get(num - 1, 0)
            right = d.get(num + 1, 0)
            total = left + right + 1
            d[num] = total
            d[num - left] = total
            d[num + right] = total
            counter[total] += 1
            counter[left] -= 1
            counter[right] -= 1
            if counter[m]:
                ans = i
        return ans
