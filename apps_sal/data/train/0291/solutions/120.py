class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = []
        ans = 0
        odd = 0
        even = 0
        tot = 0
        for i in range(len(arr)):
            tot += arr[i]
            if tot % 2 == 0:
                even += 1
            else:
                odd += 1

            count.append((tot, even, odd))
            if count[i][0] % 2 != 0:
                ans += 1
                ans += count[i][1]
            else:
                ans += count[i][2]

        return ans % (10**9 + 7)
