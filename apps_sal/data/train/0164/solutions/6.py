class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if k >= (n - 1) * n // 2:
            return ''.join(sorted(num))

        ans = []
        while k and num:
            for d in '0123456789':
                i = num.find(d)
                if 0 <= i <= k:
                    ans.append(d)
                    num = num[:i] + num[i + 1:]
                    k -= i
                    break

        return ''.join(ans) + num
