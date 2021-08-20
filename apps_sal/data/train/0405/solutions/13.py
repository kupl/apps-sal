class Solution:

    def new21Game(self, N: int, K: int, W: int) -> float:
        if N >= K + W - 1:
            return 1
        if N < K:
            return 0
        if K == 0:
            return 1
        probs = [0] * (W + 2)
        probs[0] = 1
        probs[1] = 1 / W
        for i in range(1, K):
            probs[(i + 1) % (W + 2)] = probs[i % (W + 2)] * (W + 1) / W - probs[(i + 2) % (W + 2)] / W
        for i in range(W):
            probs[(K + i + 1) % (W + 2)] = probs[(K + i) % (W + 2)] - probs[(K + i + 2) % (W + 2)] / W
        if K % (W + 2) < (N + 1) % (W + 2):
            return sum(probs[K % (W + 2):(N + 1) % (W + 2)])
        else:
            return sum(probs[K % (W + 2):]) + sum(probs[:(N + 1) % (W + 2)])
