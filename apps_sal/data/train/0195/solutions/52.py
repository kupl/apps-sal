from collections import defaultdict


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        mp = defaultdict(int)
        mask = (1 << 16) - 1
        for x in A:
            y = mask ^ x
            s = y
            while s:
                mp[s] += 1
                s = (s - 1) & y
        n = len(A)
        cnt = 0
        for i in range(n):
            if A[i] == 0:
                cnt += n * n
                continue
            for j in range(n):
                if A[i] & A[j] == 0:
                    cnt += n
                    continue
                cnt += mp[A[i] & A[j]]
        return cnt
