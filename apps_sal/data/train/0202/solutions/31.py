class Solution:
    def longestMountain(self, A: List[int]) -> int:
        up = down = ans = 0
        for i in range(1, len(A)):
            if A[i - 1] == A[i]:
                up = down = 0
            elif A[i - 1] < A[i]:
                if down or up == 0:
                    up = 2
                    down = 0
                else:
                    up += 1
            else:
                down += 1
            if up and down:
                ans = max(ans, up + down)
        return ans

        '''
        up = down = ans = 0
        for i in range(1, len(A)):
            if A[i-1]>A[i] and up:
                down += 1
            if A[i-1]==A[i] or A[i-1]<A[i] and down or i==len(A)-1:
                if up and down:
                    ans = max(ans, up+down)
                up = down = 0
            if A[i-1]<A[i]:
                up = 2 if not up else up+1

        return ans
        '''

        '''
        l = ans = 0
        phase = 0 
        for r in range(1, len(A)):
            if phase==0:
                if A[r-1]==A[r]:
                    l = r
                elif A[r-1]>A[r]:
                    if l+1<r:
                        phase = 1
                    else:
                        l = r
            if phase==1:
                if A[r-1]<=A[r] or r==len(A)-1:
                    ans = max(ans, r-l)
                    if r==len(A)-1 and A[r-1]>A[r] and r-l==ans:
                        ans += 1
                    l = r if A[r-1]==A[r] else r-1
                    phase = 0
                          
        return ans
        '''
