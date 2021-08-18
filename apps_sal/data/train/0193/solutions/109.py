class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = sorted(Counter(arr).values(), reverse=1)
        target = (len(arr)) // 2
        res = curr = 0
        for val in count:
            curr += val
            res += 1
            if curr >= target:
                break
        return res
