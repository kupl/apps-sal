class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # result = 0
        # for i in range(len(A)):
        #     for j in range(i+1,len(A)):
        #         if A[i]<=A[j]:
        #             result = max(result,j-i)
        # return result
        # Brute Force, Time Limit Exceeded

        # two pointer
        #         rMax = [0]*len(A)
        #         rMax[-1] = A[-1]
        #         for i in range(len(A)-1)[::-1]:
        #             rMax[i] = max(rMax[i+1],A[i])
        #         L=R=0
        #         result=0

        #         while R<len(A):
        #             print(L,R,result)
        #             while L<R and A[L]>rMax[R]:
        #                 L+=1
        #             result = max(result,R-L)
        #             R+=1

        #         return result

        Aindex = [(a, i) for i, a in enumerate(A)]
        Aindex.sort(key=lambda x: (x[0], x[1]))
        mn = len(A)
        ans = 0
        for a, i in Aindex:
            print((i, ans, i - mn, mn))
            ans = max(ans, i - mn)
            mn = min(mn, i)
        return ans

        # stack = []
        # res = 0
        # for i in range(len(A))[::-1]:
        #     #print(i,stack)
        #     if not stack or A[i] > stack[-1][0]:
        #         stack.append([A[i], i])
        #     else:
        #         j = stack[bisect.bisect(stack, [A[i], i])][1]
        #         print(stack,[A[i], i],bisect.bisect(stack, [A[i], i]),j)
        #         res = max(res, j - i)
        # return res

        # s = []
        # res = 0
        # for i, a in enumerate(A):
        #     if not s or A[s[-1]] > a:
        #         s.append(i)
        # print(s)
        # for j in range(len(A))[::-1]:
        #     while s and A[s[-1]] <= A[j]:
        #         res = max(res, j - s.pop())
        # return res
