class Solution:

    def minOperations(self, a: List[int]) -> int:
        ans = 0
        zero_cnt = 0
        while zero_cnt < len(a):
            zero_cnt = 0
            for (i, x) in enumerate(a):
                if x % 2 == 1:
                    ans += 1
                    a[i] = (x - 1) // 2
                else:
                    a[i] = x // 2
                zero_cnt += a[i] == 0
            ans += zero_cnt < len(a)
        return ans
