# Rem of sum is Num
# Reviewing problem


from collections import defaultdict


def cnt_func(X):
    res = 0
    right = 0
    L = len(X)
    for i in range(L):
        while right+1 < L and X[right+1] < K+X[i]:
            right += 1
        res += right-i
    return res


N, K = map(int, input().split())

A = list(map(int, input().split()))
A.insert(0, 0)
for i in range(1, N+1):
    A[i] += A[i-1]
B = [0 for i in range(N+1)]
for i in range(N+1):
    B[i] = (A[i]-i) % K
ans = 0
Mod = defaultdict(list)
for i in range(N+1):
    Mod[B[i]].append(i)
for X in Mod.values():
    ans += cnt_func(X)
print(ans)
