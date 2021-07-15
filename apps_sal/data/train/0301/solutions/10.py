class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        b_dict = {}
        for idx, b in enumerate(B):
            if b not in b_dict:
                b_dict[b] = []
            b_dict[b].append(idx)
        a_ptrs = []
        for key in b_dict:
            b_dict[key].reverse()
        for a in A:
            if a in b_dict:
                a_ptrs = a_ptrs + b_dict[a]
        lis = []
        for idx, a in enumerate(a_ptrs):
            lis_len = 0
            for i in reversed(range(idx)):
                if a_ptrs[i] < a:
                    lis_len = max(lis_len, lis[i])
            lis_len += 1
            lis.append(lis_len)
        if len(lis) == 0:
            return 0
        return max(lis)
