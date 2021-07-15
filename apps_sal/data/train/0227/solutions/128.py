from collections import deque
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        q=deque()
        cnt=0
        max_cnt=0
        for i in range(len(A)):
            if A[i]==0:
                q.append(i)
                if len(q)>K:
                    max_cnt=max(max_cnt,cnt)
                    cnt=i-q[0]
                    q.popleft()
                else:
                    cnt+=1
            else:
                cnt+=1
        max_cnt=max(max_cnt,cnt)
        return max_cnt
