N = int(input()); c = sorted(map(int, input().split())); m = 10**9 + 7; print(sum([c[i] * (N - i + 1) * pow(4, N - 1, m) for i in range(N)]) % m)
