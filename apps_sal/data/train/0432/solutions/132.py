class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.defaultdict(int)
        nums.sort()
        for n in nums:
            if count[n] == 0:
                for i in range(1,k):
                    count[n+i] += 1
            else:
                count[n] -= 1
        for c in count.values():
            if c>0:
                return False
        return True
