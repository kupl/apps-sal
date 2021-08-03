class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        queue = collections.deque()
        piles.sort()
        for ele in piles:
            queue.append(ele)

        while len(queue):
            queue.popleft()
            queue.pop()
            ans += queue.pop()

        return ans
