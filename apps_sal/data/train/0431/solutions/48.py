class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:

        MOD = 10**9 + 7
        cl = []
        stack = []
        for i in range(len(A)):

            while stack and A[stack[-1]] > A[i]:
                stack.pop()

            if not stack:
                l = i + 1
            else:
                l = i - stack[-1]
            cl.append(l)
            stack.append(i)

        cr = []
        stack = []
        for i in range(len(A) - 1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()

            if not stack:
                r = len(A) - i
            else:
                r = stack[-1] - i

            stack.append(i)
            cr.append(r)

        cr = cr[::-1]

        tot = 0
        for i in range(len(A)):
            tot += A[i] * cl[i] * cr[i]
            tot %= 10**9 + 7

        return tot
        '''
        queue = deque()
        MOD = 10**9 + 7
        
        tot = 0
        for indx, num in enumerate(A):
            tot += num
            queue.append((num,indx+1))
            
        while queue:
            sub_min, indx = queue.popleft()
            if indx < len(A):
                new_sub_min = min(sub_min, A[indx])
                queue.append((new_sub_min, indx+1))
                tot += new_sub_min
                tot %= MOD
        
        return tot
        '''
