class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        
        def help(k):
            res = 0
            left = 0
            d = {}
            for i, ele in enumerate(A):
                d[ele] = d.get(ele, 0) + 1
                while len(d) > k:
                    d[A[left]] -= 1
                    if d[A[left]] == 0:
                        del d[A[left]]
                    left += 1
                res += i - left
            return res
        
        return help(K) - help(K - 1)
