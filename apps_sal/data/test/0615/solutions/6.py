N = int(input())
A = list(map(int, input().split()))
AA = [0] * N
AA[0] = A[0]
for i in range(1, N):
    AA[i] = AA[i - 1] + A[i]
l = 0
r = 2
p = []
for m in range(1, N - 2):
    sl = AA[m]
    sr = AA[N - 1] - sl
    while abs(sl - 2 * AA[l]) > abs(sl - 2 * AA[l + 1]):
        l += 1
    while abs(AA[N - 1] + sl - 2 * AA[r]) > abs(AA[N - 1] + sl - 2 * AA[r + 1]):
        r += 1
    P = AA[l]
    Q = sl - P
    R = AA[r] - sl
    S = sr - R
    ans = max(P, Q, R, S) - min(P, Q, R, S)
    p.append(ans)
print(min(p))
