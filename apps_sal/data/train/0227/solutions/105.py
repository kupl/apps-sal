class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        s,e,z,l = 0,0,0,0
        ans = 0
        while e<len(A):
            if A[e] == 0:
                z += 1
            while z>K:
                if A[s] == 0:
                    z -= 1
                s += 1
                l -= 1
            l += 1
            ans = max(ans, l)
            e += 1
        return ans
