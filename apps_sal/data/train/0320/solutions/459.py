class Solution:
    def minOperations(self, nums: List[int]) -> int:

        ans = 0

        def cal1(arr):
            z = 0
            op = 0
            for i in range(len(arr)):
                if arr[i] % 2 == 1:
                    arr[i] -= 1
                    op += 1
                    if arr[i] == 0:
                        z += 1
            return op, z

        def cal2(arr):
            flg = 0
            for i in range(len(arr)):
                if arr[i] % 2 == 0 and arr[i] > 0:
                    arr[i] //= 2
                    flg = 1
            return flg

        nz = sum([1 for i in nums if i != 0])
        while nz > 0:
            op, z = cal1(nums)
            ans += op
            nz -= z
            ans += cal2(nums)

        return ans
