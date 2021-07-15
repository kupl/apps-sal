class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # 这道题是hulu2019年网测第二题 改成了最大值。
        # medium难度。除了暴力O(n**2) 对于每个i，右侧逐渐从i到n-1
        # 更好的办法是单调栈或者dp 时间复杂度O(n)或者O(nlogn)
        '''
        # increasing stacks,注意是subarray问题，所以是连续的一部分
        n = len(A)
        mod = 10 ** 9 + 7
        left, right = [0]*n, [0]*n
        #left[i]表示A[i]左侧，严格大于的长度
        #right[i]表示A[i]右侧，大于的长度
        #为什么，因为担心遇到连续的重复例如2，5，4，4，6 ，因此可以去掉重复部分
        #谨记，可重复出现的数组里，为了区分最小的数量，左右单调性要求不同
        s1, s2 = [], []
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([A[i],count])
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append([A[i],count])
        return sum(a*l*r for a,l,r in zip(A,left,right)) % mod
        '''
        res = 0
        s = []  # 最小值就用单调递增栈，每一个加进来的栈都是区域最小的，因为最大的被pop了
        # 递增栈的一个特点就是左右都用0最后栈会清空而且第一个0长期存在可以不用考虑stack空的问题
        A = [0] + A + [0]  # 都是大于1的数字，找最小值0没关系，反正两侧而且可以抵消因为*0
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10 ** 9 + 7)
