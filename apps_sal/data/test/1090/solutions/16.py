N, K = map(int, input().split())
S = input()
print(min(sum(S[n] == S[n + 1] for n in range(N - 1)) + 2 * K, N - 1))
