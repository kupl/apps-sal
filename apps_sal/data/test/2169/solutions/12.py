def main():
    (H, W, D) = list(map(int, input().split()))
    A = []
    for h in range(H):
        for (w, a) in enumerate(map(int, input().split())):
            A += [[a, h, w]]
    A.sort(key=lambda x: x[0])
    B = [0] * (H * W)
    for i in range(D):
        while i + D < W * H:
            B[i + D] = B[i] + abs(A[i][1] - A[i + D][1]) + abs(A[i][2] - A[i + D][2])
            i += D
    for q in range(int(input())):
        (l, r) = list(map(int, input().split()))
        print(B[~-r] - B[~-l])


main()
