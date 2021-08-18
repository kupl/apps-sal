class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        '''
        n = len(A)
        mod = 10 ** 9 + 7
        left, right = [0]*n, [0]*n
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
        s = []
        A = [0] + A + [0]
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10 ** 9 + 7)
