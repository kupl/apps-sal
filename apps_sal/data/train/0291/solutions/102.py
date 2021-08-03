import copy


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = (10**9) + 7
        arr1 = arr.copy()
        for i in range(1, len(arr)):
            arr1[i] += arr1[i - 1]

        odd, even = 0, 0
        cou = 0
        for i in range(len(arr1)):

            if arr1[i] % 2 == 0:
                even += 1
            else:
                odd += 1
        for i in range(len(arr1)):

            if arr1[i] % 2 == 1:
                cou += 1

        cou += odd * even

        return cou % mod
