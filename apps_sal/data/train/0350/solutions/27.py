class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        last_seen = {}
        start = end = 0
        ans = 0
        for i, x in enumerate(A):
            last_seen[x] = i
            while len(last_seen)>K:
                if last_seen[A[start]]==start:
                    del last_seen[A[start]]
                start += 1
            while A[end] not in last_seen or last_seen[A[end]]!=end:
                end += 1
            if len(last_seen)==K: ans += end - start + 1
        return ans

