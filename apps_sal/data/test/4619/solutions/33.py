

def main():
    W, H, N = list(map(int, input().split()))
    X = Y = 0
    for i in range(N):
        x, y, a = list(map(int, input().split()))
        if a == 1:
            X = max(X, x)
        elif a == 2:
            W = min(W, x)
        elif a == 3:
            Y = max(Y, y)
        else:
            H = min(H, y)
    print((max(W - X, 0) * max(H - Y, 0)))


main()
