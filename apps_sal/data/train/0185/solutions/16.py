class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        arr_2 = ['0', '1']
        m = k - 1
        while m != 0:
            arr_2 = ['0' + i for i in arr_2] + ['1' + i for i in arr_2]
            m -= 1
        for i in range(2 ** k):
            if arr_2[i] in s:
                continue
            else:
                return False
        return True
