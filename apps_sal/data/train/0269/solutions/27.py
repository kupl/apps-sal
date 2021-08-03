class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        temp = 0
        increment = False
        one_checked = False
        for i in nums:
            if one_checked and i != 1:
                temp += 1
            print(temp, i)
            if i == 1:
                if one_checked and temp < k:
                    return False
                temp = 0
                one_checked = True

        return True
