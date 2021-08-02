N = int(input())
A = tuple(map(int, input().split()))


def calc(B):
    P, Q = B[0], B[1]
    ret = [None] * N
    ret[1] = (P, Q)
    mid = 1

    for right in range(2, N - 2):
        Q += B[right]
        while mid < right:
            newP = P + B[mid]
            newQ = Q - B[mid]

            if abs(newP - newQ) >= abs(P - Q):
                break
            mid += 1
            P = newP
            Q = newQ

        ret[right] = (P, Q)

    return ret


left = calc(A)[1: -2]
right = calc(A[:: -1])[1: -2][:: -1]

ans = 10**10
for (P, Q), (R, S) in zip(left, right):
    ans = min(ans, abs(max(P, Q, R, S) - min(P, Q, R, S)))

print(ans)
