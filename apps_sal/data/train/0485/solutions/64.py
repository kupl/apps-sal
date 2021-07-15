class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        # 谷歌面经。给定你一个01序列。然后每次可以连续K个数进行翻转。问你最少操作次数使得全0
        # 这道题是一道贪心题。因为A[0]翻转不翻转只有唯一的一个办法。
        # 空间上考虑A只有01元素。因此可以利用这个特点避免使用额外空间
        cur, res, n = 0, 0, len(A)
        # cur means the numbers of flips in the current sliding window of size K
        # in the window, if the cur is even and A[i] = 0,we need to flip
        # if the cur is odd and A[i] = 1,we need to flip
        # we want to flip A[i], from 0 to 2, from 1 to 3.when go out window, we change it back
        for i in range(n):
            if i >= K and A[i - K] > 1:
                A[i - K] -= 2
                cur -= 1   # 维持滑动窗口
            if (cur & 1) ^ A[i] == 0:  # 根据前面的分析，这个时候我们需要替换当前的A[i]
                if i + K > len(A):   # 不过此时有一个特别注意，那就是超界（没有等号）
                    return -1
                A[i] += 2
                cur += 1
                res += 1
        # print(A)  最后窗口内的还是没完全改回来，不过问题不大
        return res
