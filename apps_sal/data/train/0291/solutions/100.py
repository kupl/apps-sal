class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        if N == 0:
            return 0
        elif N == 1:
            return abs(arr[0]) % 2
        s = 0
        tot = 0
        ct_odd = 0
        ct_even = 0
        for i in range(N):
            s += arr[i]
            if s % 2 == 1:
                tot += 1 + ct_even
                ct_odd += 1
            else:
                tot += ct_odd
                ct_even += 1
        return tot % (10 ** 9 + 7)
        'l1 = 0\n        l2 = 0\n        if(arr[0]%2):\n            l1 += 1\n        else:\n            l2 += 1\n        tot = 0\n        tot += l1\n        \n        for i in range(1,N):\n            l3 = 0\n            l4 = 0\n            if(arr[i]%2):\n                l3 = 1+l2\n                l4 = l1\n            else:\n                l3 = l1\n                l4 = 1+l2\n            l2 = l4\n            l1 = l3\n            tot += l1\n        return tot%(10**9+7)'
