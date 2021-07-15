class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [float('-inf')] + A + [float('-inf')]
    # The -inf at the beginning makes sure that the stack is never empty. The
    # -inf at the end makes sure that every element in the original A gets
    # popped from the stack eventually.
        stack = [0]
        res = 0
        
        for i in range(1, len(A)):
            while A[i] < A[stack[-1]]:
                j = stack.pop()
                k = stack[-1]
                res += A[j] * (i - j) * (j - k)
    #eg.两个区间会有一个重合，在j， 比如j点A等于3， 这样就可算上subarray [3] 了
                res %= 10 ** 9 + 7
            stack.append(i)
        return res
        
'''
        if not A:
            return 0
        curmin = []
        res = 0
        for i in A:
            curminlevel = []
            if not curmin:
                curminlevel.append(i)
                res += i
            else:
                for j in range(len(curmin[-1])):
                    minnum = min(curmin[-1][j], i)
                    curminlevel.append(minnum)
                    res += minnum
                curminlevel.append(i)
                res += i
            curmin.append(curminlevel)
        return res%(10**9 + 7)'''
                    

