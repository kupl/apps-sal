import sys
def MI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


N, K, Q = MI()
A = LI()

ans = 10**18
for i in range(N):
    a = A[i]
    left, right = 0, 0
    X = []
    while right < N:
        if A[right] >= a:
            right += 1
        else:
            if right - left >= K:
                Y = A[left:right]
                Y.sort()
                for j in range(right - left - K + 1):
                    X.append(Y[j])
            right += 1
            left = right
    if right - left >= K:
        Y = A[left:right]
        Y.sort()
        for j in range(right - left - K + 1):
            X.append(Y[j])
    if len(X) < Q or min(X) != a:
        continue
    X.sort()
    ans = min(ans, X[Q - 1] - a)

print(ans)
