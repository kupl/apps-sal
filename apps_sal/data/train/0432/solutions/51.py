class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) < k or len(nums) % k:
            return False
        cnts = defaultdict(int)
        for n in nums:
            cnts[n] += 1
        for n in sorted(list(cnts.keys())):
            if cnts[n] > 0:
                for i in range(1, k):
                    if n + i not in cnts or cnts[n + i] < cnts[n]:
                        return False
                    cnts[n + i] -= cnts[n]
        return True
