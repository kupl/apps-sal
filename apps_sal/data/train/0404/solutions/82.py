# A[1~N] K (1 <= K <= N)
# 
# B[m][w] = 前A[1~m]分w組的最大平均值總和
# 
# B[m][w] = max(B[m-1][w-1] + A[m]
#               B[m-2][w-1] + (A[m-1]+A[m])/2
#               B[m-3][w-1] + (A[m-2 ~ m])/3

class Solution:
  def largestSumOfAverages(self, A, K):
    N = len(A)
    S = [0] * (1 + N)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + A[i - 1]
    B = []
    for i in range(1 + N):
      B.append([0] * (1 + K))
    for m in range(1, N + 1):     # m : 剩餘人數
        for w in range(1, K + 1): # w : 剩餘組數
            if w == 1:
                B[m][w] = S[m] / m
                continue
            if m < w:
                break
            B[m][w] = -1000000
            for e in range(1, m - w + 2): # e : 最後一組的人數
                B[m][w] = max(B[m][w], B[m - e][w - 1] +
                                       (S[m] - S[m - e]) / e)
            # print('B[%d][%d] = %f' % (m, w, B[m][w]))
    return B[N][K]

