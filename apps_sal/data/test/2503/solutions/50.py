import numpy as np
# from time import time

# t0 = time()
N, K = list(map(int, input().split()))
B = np.zeros((2 * K, 2 * K), np.int32)
W = np.zeros((2 * K, 2 * K), np.int32)
# t1 = time()
# print(t1 - t0)
for _ in range(N):
    x, y, c = input().split()
    if c == "B":
        B[int(x) % (2 * K)][int(y) % (2 * K)] += 1
    else:
        W[int(x) % (2 * K)][int(y) % (2 * K)] += 1
# t2 = time()
# print(t2 - t1)
SB = np.zeros((4 * K + 1, 4 * K + 1), np.int32)
SW = np.zeros((4 * K + 1, 4 * K + 1), np.int32)
# t3 = time()
# print(t3 - t2)
SB[0*K+1:2*K+1, 0*K+1:2*K+1] = B
SB[0*K+1:2*K+1, 2*K+1:4*K+1] = B
SB[2*K+1:4*K+1, 0*K+1:2*K+1] = B
SB[2*K+1:4*K+1, 2*K+1:4*K+1] = B
SW[0*K+1:2*K+1, 0*K+1:2*K+1] = W
SW[0*K+1:2*K+1, 2*K+1:4*K+1] = W
SW[2*K+1:4*K+1, 0*K+1:2*K+1] = W
SW[2*K+1:4*K+1, 2*K+1:4*K+1] = W
# t4 = time()
# print(t4 - t3)
np.cumsum(SB, 0, out=SB)
np.cumsum(SB, 1, out=SB)
np.cumsum(SW, 0, out=SW)
np.cumsum(SW, 1, out=SW)
# t5 = time()
# print(t5 - t4)
ans = 0
cand = SB[1*K:3*K+1, 1*K:3*K+1].copy()
cand -= SB[0*K:2*K+1, 1*K:3*K+1]
cand -= SB[1*K:3*K+1, 0*K:2*K+1]
cand += SB[0*K:2*K+1, 0*K:2*K+1]
cand += SB[2*K:4*K+1, 2*K:4*K+1]
cand -= SB[1*K:3*K+1, 2*K:4*K+1]
cand -= SB[2*K:4*K+1, 1*K:3*K+1]
cand += SB[1*K:3*K+1, 1*K:3*K+1]
cand += SW[2*K:4*K+1, 1*K:3*K+1]
cand -= SW[1*K:3*K+1, 1*K:3*K+1]
cand -= SW[2*K:4*K+1, 0*K:2*K+1]
cand += SW[1*K:3*K+1, 0*K:2*K+1]
cand += SW[1*K:3*K+1, 2*K:4*K+1]
cand -= SW[0*K:2*K+1, 2*K:4*K+1]
cand -= SW[1*K:3*K+1, 1*K:3*K+1]
cand += SW[0*K:2*K+1, 1*K:3*K+1]
ans = np.max(cand)
# t6 = time()
# print(t6 - t5)

print(ans)

