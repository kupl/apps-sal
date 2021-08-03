class Solution:
    '''
    [3,2,2,4] 1 -> [2,2,2,4] 1 -> [1,1,1,2] 3 -> [0,0,0,2] 1 -> [0,0,0,1] 1 -> [0,0,0,0]
    '''

    def minOperations(self, nums: List[int]) -> int:
        if nums == [0]:
            return 0

        copy = list(nums)
        ans = 0
        while any([el != 0 for el in copy]):
            numOdd = 0
            for i in range(len(copy)):
                if copy[i] % 2 != 0:
                    numOdd += 1
                    copy[i] -= 1

            for i in range(len(copy)):
                copy[i] /= 2

            ans += numOdd + 1
        return ans - 1
