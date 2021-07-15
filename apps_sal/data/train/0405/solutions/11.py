class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        #probability of falling into [K, K + 1, ..., N]
        #P[i] = 1/W*(P[i - 1] + ... + P[i - W])
        #running_sum: P[i - 1] + ... + P[i - W]
        if K == 0:
            return 1
        running_sum = 1
        P = [1]
        for i in range(1, W):
            P.append(1/W * running_sum)
            running_sum += P[-1]
        # print(P)
        for i in range(W, K):
            P.append(1/W * running_sum)
            running_sum += (P[-1] - P[i-W])
        # print(P)
        res = 0
        #17: = 1/W*(P[7] + ... + P[16])
        #18: = 1/W*(P[8] + ... + P[16])
        #19: = 1/W*(P[9] + ... + P[16])
        
        #At 7: 1/W chance (7 + 10)
        #8: 2/W chance (8 + 9, 8 + 10)
        #9: 3/W (9 + 8, 9 + 9, 9 + 10)
        #15: 5/W (15 + 2, ..., 15 + 6)
        #16: 5/W   (16 + 1, ..., 16 + 5)
        running_sum = sum(P[max(0, K - W): K])
        # print(sum(P[0:1]))
        # print(\"running_sum = {0}\".format(running_sum))
        # print(sum(P[7:17]) + sum(P[8:17]) + sum(P[9:17]) + sum(P[10:17]) + sum(P[11:17]))
        # print(1*P[7] + 2*P[8] + 3*P[9] + 4*P[10] + 5*sum(P[11:17]))
        
        #12: (P[2] + ... + P[11])*1/W
        #13: (P[3] + ... + P[11])*1/W
        #14: (P[4] + ... + P[11])*1/W
        print(sum(P[2:12]) + sum(P[3:12]) + sum(P[4:12])+  sum(P[5:12]) + sum(P[6:12]) + sum(P[7:12]) + sum(P[8:12]) + sum(P[9:12]) + sum(P[10:12]) + sum(P[11:12]))
        #From 2: 2 + 10
        #From 3: 3 + 9, 3 + 10
        #From 4: 4 + 8, 4 + 9, 4 + 10
        #From 11: 11 + 1, ..., 11 + 10
        
        
        #Last number candidates: From max(0, K - W) to K - 1
        #From candidate i, we can go from max(i + 1, K) to min(i + W, N) 
        #so there are min(i + W, N) - max(i + 1, K) + 1 options
        for i in range(max(0, K - W), K):
            #from i: can go from max(i + 1, K) to min(i + 10, N)
            res += P[i]/W * max((min(i + W, N) - max(i + 1, K) + 1), 0)
            # print(res)
        # for i in range(K, min(N + 1, K + W)):
        #     res += (1/W * running_sum)
        #     if i >= W:
        #         running_sum -= P[i - W]
        # # print(sum(P[1:11]))
        return res
