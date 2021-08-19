class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        print(count)
        nums.sort()
        for x in nums:
            if count[x] == 0:
                continue
            else:
                for i in range(1, k):
                    print(x, x + i)
                    if count[x + i] > 0:
                        count[x + i] -= 1
                    elif count[x - i] > 0:
                        count[x - i] -= 1
                    else:
                        return False
            count[x] -= 1
        return True
