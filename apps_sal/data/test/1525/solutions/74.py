h, w, k = map(int, input().split())
mod = 10**9 + 7
R = [[], [1], [1, 1], [2, 1, 2], [3, 2, 2, 3], [5, 3, 4, 3, 5], [8, 5, 6, 6, 5, 8], [13, 8, 10, 9, 10, 8, 13]]
T = [1, 2, 3, 5, 8, 13, 21, 34]
r = R[w - 1]
t = T[w - 1]
A = [0] * w
A[0] = 1
if w == 1:
    print(1)
else:
    for i in range(h):
        C = [0] * w
        for i in range(w):
            if i == 0:
                C[0] += (t - r[0]) * A[0]
                C[1] += r[0] * A[0]
            elif i == w - 1:
                C[w - 1] += (t - r[w - 2]) * A[w - 1]
                C[w - 2] += r[w - 2] * A[w - 1]
            else:
                C[i - 1] += r[i - 1] * A[i]
                C[i] += (t - r[i - 1] - r[i]) * A[i]
                C[i + 1] += r[i] * A[i]
        for i in range(w):
            C[i] %= mod
        A = C
    print(A[k - 1])
