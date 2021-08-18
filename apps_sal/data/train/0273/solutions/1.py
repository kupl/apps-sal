class Solution:
    def racecar(self, target: int) -> int:
        dist = [float('inf')] * (target + 1)
        dist[0] = 0

        for t in range(1, target + 1):
            k = t.bit_length()
            up_limit = 2**k - 1
            if t == up_limit:
                dist[t] = k

            for j in range(1, k):
                for q in range(j):
                    dist[t] = min(dist[t], dist[t - 2**j + 2**q] + j + 1 + q + 1)

            dist[t] = min(dist[t], dist[2**k - 1 - t] + k + 1)

        return dist[target]
