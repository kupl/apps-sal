N, M, Q = list(map(int, input().split()))
A = []

for i in range(Q):
    A.append(list(map(int, input().split())))


def calc(B, n):
    ans = 0
    # not enough length
    if len(B) < N:
        for i in range(n, M + 1):
            ans = max(ans, calc(B + [i], i))
    # enough length
    else:
        #print("B:", B)
        for j in range(Q):
            if B[A[j][1] - 1] - B[A[j][0] - 1] == A[j][2]:
                ans += A[j][3]
        #print("ans:", ans)
    return ans


print((calc([], 1)))
