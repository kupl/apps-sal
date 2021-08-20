N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))
L = [0] * (sum(T) * 2 + 1)
R = [0] * (sum(T) * 2 + 1)
(xt, xv) = (0, 0)
for (t, v) in zip(T, V):
    for tt in range(xt * 2 + 1, (t + xt) * 2 + 1):
        xv += 0.5
        L[tt] = min(v, xv)
    xt += t
    xv = min(v, xv)
(xt, xv) = (0, 0)
for (t, v) in zip(T[::-1], V[::-1]):
    for tt in range(xt * 2 + 1, (t + xt) * 2 + 1):
        xv += 0.5
        R[tt] = min(v, xv)
    xt += t
    xv = min(v, xv)
print(sum(map(min, L, R[::-1])) / 2)
