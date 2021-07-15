class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        deque = collections.deque()
        deque.append(1)
        ans = 0
        for num in nums:
            if num % 2 == 0:
                deque[-1] += 1
                continue
            if len(deque) == k + 1:
                ans += deque[0] * deque[-1]
                deque.popleft()
            deque.append(1)
        if len(deque) == k + 1:
            ans += deque[0] * deque[-1]
        return ans
