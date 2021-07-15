class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        val2idx = {val: i for i, val in enumerate(A)}
        longest = collections.defaultdict(lambda: 2) #defaultval为2
        longest[(0,0)] = 1
        res = 0
        for k in range(2, len(A)):
            for j in range(k):
                i = val2idx.get(A[k] - A[j], None)
                if i != None and i < j: # i < j to control increasing order
                    longest[(j,k)] = longest[(i,j)] + 1
                    res = max(res, longest[(j,k)])
        return res if res >= 3 else 0
        # 不能只用一个数字做为ending。比如[1,2,3,4].如果只用一个数字，那么end为3时候longest是3，但是end为4的时候实际上是[1,3,4],而不是[1,2,3,4],不能直接end3 + 1

