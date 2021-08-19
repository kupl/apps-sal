def main():
    (N, X, *M) = list(map(int, open(0).read().split()))
    print(N + (X - sum(M)) // min(M))


main()
