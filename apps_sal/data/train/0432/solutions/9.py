class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if not nums or not k:
            return False
        c = Counter(nums)
        while c:
            num = sorted(c.keys())[0]
            for i in range(k):
                if num + i in c and c[num + i] > 0:
                    c[num + i] -= 1
                    if c[num + i] == 0:
                        del c[num + i]
                else:
                    return False
        return True
