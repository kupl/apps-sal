class Solution:
    def racecar(self, target: int) -> int:
        dist = [float('inf')] * (target + 1)
        dist[0] = 0  # the minimum number of steps to achieve i with starting speed being 1
        #dist[1] = 1
        #dist[2] = 4
        #dist[3] = 2

        for t in range(1, target + 1):
            k = t.bit_length()
            up_limit = 2**k - 1
            if t == up_limit:  # right on the target by only move forward with no reverse
                dist[t] = k

            # between two critical points (k-1 steps and k steps)
            # the last move is forward move
            # in this case there should be even number of turns, which results in odd number of consecutive acceleration period. To recurse into the original problem (starting speed is 1 and point to the target) we need to remove the first two turns (or last two turns)
            for j in range(1, k):
                for q in range(j):
                    dist[t] = min(dist[t], dist[t - 2**j + 2**q] + j + 1 + q + 1)  # the last move is forward

            dist[t] = min(dist[t], dist[2**k - 1 - t] + k + 1)  # the last move is backward

        return dist[target]
