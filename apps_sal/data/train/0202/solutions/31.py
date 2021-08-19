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
        '\n        up = down = ans = 0\n        for i in range(1, len(A)):\n            if A[i-1]>A[i] and up:\n                down += 1\n            if A[i-1]==A[i] or A[i-1]<A[i] and down or i==len(A)-1:\n                if up and down:\n                    ans = max(ans, up+down)\n                up = down = 0\n            if A[i-1]<A[i]:\n                up = 2 if not up else up+1\n\n        return ans\n        '
        '\n        l = ans = 0\n        phase = 0 #0:ascend, 1: descend\n        for r in range(1, len(A)):\n            if phase==0:\n                if A[r-1]==A[r]:\n                    l = r\n                elif A[r-1]>A[r]:\n                    if l+1<r:\n                        phase = 1\n                    else:\n                        l = r\n            if phase==1:\n                if A[r-1]<=A[r] or r==len(A)-1:\n                    ans = max(ans, r-l)\n                    if r==len(A)-1 and A[r-1]>A[r] and r-l==ans:\n                        ans += 1\n                    l = r if A[r-1]==A[r] else r-1\n                    phase = 0\n                          \n        return ans\n        '
