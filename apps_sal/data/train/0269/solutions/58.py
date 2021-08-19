class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c = nums.count(1) - 1
        if c < 0:
            return True
        if c == 0:
            return True
        ini = nums.index(1)
        while c:
            fin = nums.index(1, ini + 1, len(nums))
            print(fin)
            if fin - ini < k + 1:
                return False
            c -= 1
            ini = fin
        return True
