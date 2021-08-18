
def search(start, N, X, Y):
    dist = [0 for _ in range(N)]
    if start <= X:
        for i in range(X):
            dist[i] = abs(start - i)
        for i in range(Y, N):
            dist[i] = (X - start) + 1 + (i - Y)
        for i in range(X, (Y - X) // 2 + X + 1):
            dist[i] = (i - start)
        for i in range((Y - X) // 2 + X + 1, Y):
            dist[i] = (X - start) + 1 + (Y - i)
    elif start >= Y:
        for i in range(Y, N):
            dist[i] = abs(start - i)
        for i in range(X):
            dist[i] = (start - Y) + 1 + (X - i)
        for i in range(X, (Y - X) // 2 + X):
            dist[i] = (start - Y) + 1 + (i - X)
        for i in range((Y - X) // 2 + X, Y):
            dist[i] = (start - i)
    else:
        toX = min(start - X, Y - start + 1)
        toY = min(Y - start, start - X + 1)
        dist[start] = 0
        for i in range(X):
            dist[i] = (X - i) + toX
        for i in range(Y, N):
            dist[i] = toY + (i - Y)
        for i in range(X, start):
            dist[i] = min(start - i, Y - start + 1 + i - X)
        for i in range(start + 1, Y):
            dist[i] = min(i - start, start - X + 1 + Y - i)
    return dist


def main():
    N, X, Y = [int(n) for n in input().split(" ")]

    X = X - 1
    Y = Y - 1

    lenD = []
    for i in range(N):
        d = search(i, N, X, Y)
        lenD.append(d)

    kcounter = [0 for _ in range(N - 1)]

    for i in range(N):
        for j in range(i + 1, N):
            k = lenD[i][j]
            kcounter[k - 1] += 1

    for k in kcounter:
        print(k)


main()
