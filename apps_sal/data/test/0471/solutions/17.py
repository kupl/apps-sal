N, A = list(map(int, input().split()))
X = list(map(int, input().split()))
X.sort()
if N == 1:
    print(0)
    return
elif N == 2:
    print(min(abs(X[0] - A), abs(X[1] - A)))
    return
ans = int(1e18)
ans = min(ans, abs(X[N-2] - X[0]) + min(abs(A - X[0]), abs(A - X[N-2])))
ans = min(ans, abs(X[N-1] - X[1]) + min(abs(A - X[1]), abs(A - X[N-1])))
print(ans)

