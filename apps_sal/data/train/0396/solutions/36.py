class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        N = 1
        track = dict()
        while True:
            rem = N % K
            if rem == 0:
                return len(str(N))
            if track.get(rem):
                return -1
            track[rem] = True
            N = N * 10 + 1
