def main():
    H, W, N = list(map(int, input().split()))
    C = {}
    for _ in range(N):
        a, b = list(map(int, input().split()))
        for x in range(max(2, a - 1), min(H, a + 2)):
            for y in range(max(2, b - 1), min(W, b + 2)):
                C[(x, y)] = C.get((x, y), 0) + 1
    D = list(C.values())
    print(((H - 2) * (W - 2) - len(C)))
    for j in range(1, 10):
        print((D.count(j)))


main()
