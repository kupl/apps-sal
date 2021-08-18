from functools import lru_cache


class Solution:
    def numPermsDISequence(self, S: str) -> int:
        '''
        这道题目的关键是第一步看到10**9+7知道用dp方法来做
        dp[i]表示范围[0，i]的序列个数，然后发现不好找递推关系
        这个时候肯定是隐藏的信息没用，外面需要通过实际的例子来总结影响个数的另外一个参数
        序列是升还是降跟什么关系最大，那就是最后一个数字。DID模式，我们可以是1032，那么我们再加个D，要求递减
        这个时候多出了一个4来，我们如何改造1032呢，直接加4是不行的，那么加一样的2？改成10432，相当于3，2都+1
        加1呢？改成20431，相当于1，3，2都+1，那么规律是什么。
        如果是D，那么只能放<=最后一个数的数，然后把原来所有>=尾巴的数都+1,最后一个数很重要
        反过来想，如果是I,那么只能放>最后一个数的数，然后原来所有的>=新加的数都+1
        '''
        mod = 10 ** 9 + 7
        n = len(S)

        @lru_cache(None)
        def dfs(i, j):
            if i == 0:
                return 1
            elif S[i - 1] == 'D':
                return sum(dfs(i - 1, k) for k in range(j, i)) % mod
            else:
                return sum(dfs(i - 1, k) for k in range(j)) % mod
        return sum(dfs(n, j) for j in range(n + 1)) % mod
