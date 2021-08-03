from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums = sorted(nums)

        nums_dict = Counter(nums)
        nums_set = sorted(list(nums_dict.keys()))

        while nums_set:
            i = nums_set.pop(0)
            count = nums_dict.pop(i)

            for j in range(i + 1, i + k):
                if j not in nums_dict:
                    return False
                n = nums_dict.pop(j) - count
                if n < 0:
                    return False

                elif n == 0:
                    nums_set.remove(j)

                else:
                    nums_dict[j] = n

        return True
