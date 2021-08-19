class Solution:

    def longestOnes(self, x: List[int], K: int) -> int:
        buf = collections.deque()
        n = len(x)
        i = 0
        unused = K
        start = -1
        maxlen = float('-inf')
        while i < n:
            if x[i] == 0:
                if unused > 0:
                    buf.append(i)
                    unused -= 1
                    maxlen = max(i - start, maxlen)
                elif buf:
                    start = buf.popleft()
                    maxlen = max(i - start, maxlen)
                    buf.append(i)
                else:
                    maxlen = max(i - 1 - start, maxlen)
                    start = i
            else:
                maxlen = max(i - start, maxlen)
            i += 1
        return maxlen if n > 0 else n
