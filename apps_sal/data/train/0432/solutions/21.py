class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        hm = {}
        uni_nums = []
        for num in nums:
            if num not in hm:
                hm[num] = 1
                uni_nums.append(num)
            else:
                hm[num] += 1

        uni_nums = sorted(uni_nums)
        N = len(uni_nums)
        i = 0
        while i < N:
            if hm[uni_nums[i]] == 0:
                i += 1
            else:
                pick = uni_nums[i]
                for j in range(k):
                    if pick + j not in hm or hm[pick + j] == 0:
                        return False
                    else:
                        hm[pick + j] -= 1
        return True
