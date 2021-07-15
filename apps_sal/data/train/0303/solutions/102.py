class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        L=len(arr)
        record=dict()
        record[0]=0
        for idx in range(1,L+1):
            r=-float('inf')
            for gap in range(1,k+1):
                if idx-gap<0:
                    continue
                else:
                    r=max(r,max(arr[idx-gap:idx])*gap+record[idx-gap])
            record[idx]=r
        return record[L]

