class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        lst = sorted(A)
        count = K
        i = 0
        while count > 0:
            if lst[i] <= lst[i + 1]:
                lst[i] = lst[i] * -1
                count -= 1
            else:
                i += 1
        return sum(lst)
