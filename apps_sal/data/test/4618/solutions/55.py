S = input()
K = int(input())
print(sorted(set((S[i:i + j + 1] for i in range(len(S)) for j in range(K))))[K - 1])
