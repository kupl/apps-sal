from collections import Counter
N = int(input())
*S, = map(int, input().split())
C = Counter(S)

memo = [[-1]*(N+1) for i in range(N+1)]
def comb(n, k):
    if memo[n][k] != -1:
        return memo[n][k]
    if k == 0 or n == k:
        return 1
    memo[n][k] = r = comb(n-1, k) + comb(n-1, k-1)
    return r

*CS, = C.items()
CS.sort(reverse=1)
S = [0]
for k, v in CS:
    S.append(S[-1]+v)
T = [0]
for i in range(N+1):
    T.append(T[-1]+comb(N, i))
ok = 1
if len(S) < len(T):
    ok = 0
else:
    ok = all(a <= b for a, b in zip(S, T)) and S[-2] >= 2**(N-1)
print("Yes" if ok else "No")
