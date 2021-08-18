import sys
input = sys.stdin.readline
N, X = (int(i) for i in input().split())
DP_all = [0] * (N + 1)
DP_p = [0] * (N + 1)
DP_all[0] = 1
DP_p[0] = 1

for i in range(N):
    DP_all[i + 1] = DP_all[i] * 2 + 3
    DP_p[i + 1] = DP_p[i] * 2 + 1


def p_num(L, x):
    if x <= L:
        return 0
    if x == DP_all[L]:
        return DP_p[L]
    elif x < DP_all[L] // 2 + 1:
        return p_num(L - 1, x - 1)
    elif x == DP_all[L] // 2 + 1:
        return DP_p[L - 1] + 1
    elif x > DP_all[L] // 2 + 1:
        return DP_p[L - 1] + 1 + p_num(L - 1, x - DP_all[L - 1] - 2)


ans = p_num(N, X)
print(ans)
