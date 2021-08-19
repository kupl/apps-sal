def resolve():
    (H, W) = list(map(int, input().split()))
    N = int(input())
    A = list(map(int, input().split()))
    C = [[0 for _ in range(W)] for __ in range(H)]
    color = 1
    reverse = False
    cnt = 0
    for i in range(H):
        for j in range(W):
            if reverse:
                _j = W - 1 - j
            else:
                _j = j
            C[i][_j] = color
            cnt += 1
            if cnt == A[color - 1]:
                color += 1
                cnt = 0
        reverse = not reverse
    [print(' '.join(map(str, C[i]))) for i in range(H)]


if '__main__' == __name__:
    resolve()
