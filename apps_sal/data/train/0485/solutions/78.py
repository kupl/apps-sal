class Solution:
    def minKBitFlips(self, A: List[int], k: int) -> int:

        latest_possible_flip = len(A) - k       # 4
        flipped = collections.deque()
        flips = 0
        for i in range(len(A)):
            if flipped and (flipped[0] < i):    # 3
                flipped.popleft()
            if len(flipped) & 1 == A[i]:          # 2
                if i <= latest_possible_flip:   # 4
                    flips += 1
                    flipped.append(i + k - 1)       # 1
                else:
                    return -1
        return flips
