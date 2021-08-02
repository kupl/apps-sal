S = input(); N = len(S); print(sum(S[i] != S[N - i - 1] for i in range(N // 2)))
