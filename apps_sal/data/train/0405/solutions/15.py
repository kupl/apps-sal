class Solution:

    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        if K - 1 + W <= N:
            return 1.0
        prob = [0.0] * (K + W)
        avg = 0
        for i in range(W):
            prob[K + i] = float(K + i <= N)
            avg += prob[K + i] / W
        for i in range(K)[::-1]:
            prob[i] += avg
            avg += (prob[i] - prob[i + W]) / W
        return prob[0]
