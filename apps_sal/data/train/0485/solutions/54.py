class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        cur = 0 # 到达当前位置的翻转次数
        res = 0
        for i in range(n):
            if i >= K and A[i-K] > 1:
                # 最左元素被移除窗口，所以要取消它的翻转
                cur -= 1
                A[i-K] -= 2
            if (cur % 2) == A[i]: # 翻转次数与A[i]同奇偶就需要翻转
                if i + K > n: return -1
                cur += 1
                res += 1
                A[i] += 2
        return res

