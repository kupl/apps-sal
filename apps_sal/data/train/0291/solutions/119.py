class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        pre = [0]
        for n in arr:
            pre.append(pre[-1] + n)
        odd = even = 0
        ans = 0
        for i in range(len(pre)):
            if pre[i] % 2 == 0:
                ans += odd
                even += 1
            else:
                ans += even
                odd += 1
        return ans % (10 ** 9 + 7)
