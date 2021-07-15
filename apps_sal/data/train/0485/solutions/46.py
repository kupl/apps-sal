class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        cnt=0
        dq=collections.deque()
        for i in range(len(A)):
            if A[i]==(1 if len(dq)%2 else 0):
                cnt+=1
                dq.append(i+K-1)
            if dq and dq[0]==i:
                dq.popleft()
        return -1 if len(dq) else cnt

