class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        dic = Counter(nums)
        for x in sorted(nums):
            if x in dic:
                for y in range(x, x + k):
                    if y in dic:
                        dic[y] -= 1
                        if dic[y] == 0:
                            del dic[y]
                    else:
                        return False
        return True
