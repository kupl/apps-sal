class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if l % k != 0:
            return False
        g = int(l // k)
        num_dict = dict()
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        for i in range(g):
            val = min(num_dict.keys())
            if num_dict[val] == 1:
                del num_dict[val]
            else:
                num_dict[val] -= 1
            for j in range(1, k):
                val += 1
                if val not in num_dict:
                    return False
                elif num_dict[val] == 1:
                    del num_dict[val]
                else:
                    num_dict[val] -= 1
        return True
