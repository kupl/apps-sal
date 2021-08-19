(N, X, M) = list(map(int, input().split()))
idx = [-1] * M
A = []
total = 0
length = 0
while idx[X] == -1:
    A.append(X)
    idx[X] = length
    length += 1
    total += X
    X = pow(X, 2, M)
cycle = length - idx[X]
cycle_sum = sum(A[idx[X]:length])
ans = 0
if length >= N:
    print(sum(A[:N]))
else:
    ans += total
    N -= length
    (l, m) = divmod(N, cycle)
    ans += cycle_sum * l
    ans += sum(A[idx[X]:idx[X] + m])
    print(ans)
