def match(l, r):
    L = r - l
    if L % 2 == 1: return False
    for i in range(L // 2):
        if R[P[l + i]] >= r and R[P[l + i]] != -1: return False
        if (P[l + i] == Q[l + L // 2 + i] or P[l + i] == 0 or Q[l + L // 2 + i] == 0) and Q[l + i] == P[l + L // 2 + i] == 0: continue
        return False
    return True


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
        if dp[j] == True and match(j, i):
            dp[i] = True
            break
print("Yes" if dp[-1] else "No")
