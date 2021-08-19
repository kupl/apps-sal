class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        flipped = deque()
        count = 0
        flips = 0
        for i in range(len(A)):
            if i > 0:
                x = flipped.popleft() if i >= K else 0
                count -= x
            if (A[i] + count) % 2 == 0:
                count += 1
                flipped.append(True)
                flips += 1
            else:
                flipped.append(False)
        return flips if not any(list(flipped)[1:]) else -1
