class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans, sm = 0, 0
        q = deque()

        for v in arr:
            sm += v
            q.append(v)

            if len(q) > k:
                sm -= q.popleft()

            if len(q) == k:
                ans += ((sm / k) >= threshold)

        return ans
