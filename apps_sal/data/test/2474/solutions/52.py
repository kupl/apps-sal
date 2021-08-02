N = int(input()); c = sorted(list(map(int, input().split()))); m = 10**9 + 7; print(sum([c[i] * (N - i + 1) * pow(2, 2 * N - 2, m) for i in range(N)]) % m)
