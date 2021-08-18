class Solution:
    def numberOfArithmeticSlices(self, A):
        ans = [0] * len(A)
        for i in range(0, len(A)):
            if i < 2:
                ans[i] = 0
            else:
                ans[i] = ans[i - 1]
                temp = A[:i + 1][::-1]
                for j in range(0, i - 1):
                    slice = temp[j:j + 3]
                    if self.checkArithmetic(slice):
                        ans[i] += 1
                    else:
                        break
        return 0 if len(A) == 0 else ans[-1]

    def checkArithmetic(self, slice):
        diff = slice[1] - slice[0]
        for i in range(len(slice) - 1):
            if slice[i + 1] - slice[i] != diff:
                return False
        return True
