def main():
    (N, M) = list(map(int, input().split()))
    if N % 2 == 1:
        for i in range(M):
            print((i + 1, N - i - 1))
    else:
        s = set()
        t = 0
        for i in range(M):
            (a, b) = (i + 1, N - i - t)
            if b - a in s or a + N - b in s or b - a == a + N - b:
                t += 1
                b = N - i - t
            print((a, b))
            s.add(b - a)
            s.add(N + a - b)


main()
