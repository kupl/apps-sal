class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        if N == 0:
            return 0
        elif N == 1:
            return abs(arr[0]) % 2
        l1 = 0
        l2 = 0
        if arr[0] % 2:
            l1 += 1
        else:
            l2 += 1
        tot = 0
        tot += l1
        for i in range(1, N):
            l3 = 0
            l4 = 0
            if arr[i] % 2:
                l3 = 1 + l2
                l4 = l1
            else:
                l3 = l1
                l4 = 1 + l2
            l2 = l4
            l1 = l3
            tot += l1
        return tot % (10 ** 9 + 7)
