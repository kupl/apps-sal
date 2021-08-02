def check(A, H, W):
    for h in range(H):
        for w in range(W - 1):
            if A[h][w] >= A[h][w + 1]:
                return False
    for w in range(W):
        for h in range(H - 1):
            if A[h][w] >= A[h + 1][w]:
                return False
    return True


def solve():
    H, W = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(H)]
    B = [list(map(int, input().split())) for i in range(H)]
    if check(A, H, W) and check(B, H, W):
        return 'Possible'
    for h in range(H):
        for w in range(W):
            if A[h][w] > B[h][w]:
                A[h][w], B[h][w] = B[h][w], A[h][w]
    if check(A, H, W) and check(B, H, W):
        return 'Possible'
    return 'Impossible'


print(solve())
