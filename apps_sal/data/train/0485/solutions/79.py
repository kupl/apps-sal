class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        win = collections.deque()
        ans = 0
        for (i, x) in enumerate(A):
            while len(win) > 0 and win[0] < i - K + 1:
                win.popleft()
            if x ^ len(win) % 2 == 0:
                if i + K - 1 <= len(A) - 1:
                    ans += 1
                    win.append(i)
                else:
                    return -1
        return ans
