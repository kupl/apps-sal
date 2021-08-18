class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1
        running_sum = 1
        P = [1]
        for i in range(1, W):
            P.append(1 / W * running_sum)
            running_sum += P[-1]
        for i in range(W, K):
            P.append(1 / W * running_sum)
            running_sum += (P[-1] - P[i - W])
        res = 0

        running_sum = sum(P[max(0, K - W): K])

        print(sum(P[2:12]) + sum(P[3:12]) + sum(P[4:12]) + sum(P[5:12]) + sum(P[6:12]) + sum(P[7:12]) + sum(P[8:12]) + sum(P[9:12]) + sum(P[10:12]) + sum(P[11:12]))

        for i in range(max(0, K - W), K):
            res += P[i] / W * max((min(i + W, N) - max(i + 1, K) + 1), 0)
        return res
