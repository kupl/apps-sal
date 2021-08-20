N = int(input())
A = [int(x) for x in input().split()]
(P, Q, R, S) = (A[0], 0, A[1] + A[2], sum(A[3:]))
(l, r) = (1, 3)
ans = float('inf')
for i in range(2, N - 1):
    Q += A[i - 1]
    while l < i - 1:
        if abs(P - Q) > abs(P + A[l] - (Q - A[l])):
            P += A[l]
            Q -= A[l]
            l += 1
        else:
            break
    R -= A[i - 1]
    if i == r:
        R += A[r]
        S -= A[r]
        r += 1
    while r < N - 1:
        if abs(R - S) > abs(R + A[r] - (S - A[r])):
            R += A[r]
            S -= A[r]
            r += 1
        else:
            break
    ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
print(ans)
