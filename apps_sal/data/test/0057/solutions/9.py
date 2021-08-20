def main():
    n = int(input())
    X = []
    Y = []
    for _ in range(n):
        (x, y) = list(map(int, input().split()))
        X.append(x)
        Y.append(y)
    if n == 1:
        return -1
    xleft = min(X)
    xright = max(X)
    ybot = min(Y)
    ytop = max(Y)
    if xleft != xright and ybot != ytop:
        return (ytop - ybot) * (xright - xleft)
    else:
        return -1


print(main())
