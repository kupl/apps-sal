class Solution:

    def numSubseq(self, lis: List[int], tar: int) -> int:
        n = len(lis)
        mod = 1000000000 + 7
        lis.sort()
        i = 0
        j = n - 1
        ans = 0
        tmp = pow(2, n, mod) - 1
        while i <= j:
            if lis[i] + lis[j] <= tar:
                i += 1
            else:
                ans += pow(2, j - i, mod)
                ans = ans % mod
                j -= 1
        print((tmp, ans))
        return (tmp - ans) % mod
