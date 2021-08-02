def match(l, r):
    L = r - l
    if L % 2 == 1: return 0
    for i in range(l, l + L // 2):
        if R[P[i]] >= r and R[P[i]] != -1: return 0
        if (P[i] == Q[L // 2 + i] or P[i] == 0 or Q[L // 2 + i] == 0) and Q[i] == P[L // 2 + i] == 0: continue
        return 0
    return 1


N = int(input())
P, Q = [0] * (2 * N), [0] * (2 * N)
R = [-1] * (N + 1)
for i in range(1, N + 1):
    A, B = map(int, input().split())
    if (A != -1 and P[A - 1] != 0) or (B != -1 and Q[B - 1] != 0): print("No"); return
    if A != -1: P[A - 1] = i
    if B != -1: Q[B - 1] = i; R[i] = B - 1
dp = [0] * (2 * N + 1)
dp[0] = 1
for i in range(2, 2 * N + 1):
    for j in range(i):
        if dp[j] * match(j, i): dp[i] = 1; break
print('NYoe s'[dp[-1]::2])
