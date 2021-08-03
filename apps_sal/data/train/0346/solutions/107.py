class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = list(map(lambda x: x % 2, nums))
        n = len(arr)
        arr = [0] + list(itertools.accumulate(arr))
        hm = Counter()
        res = 0
        for i in arr:
            res += hm[i]
            hm[i + k] += 1

        return res
