K = int(input())
S = input()
L = len(S)
print(S[:min(K, L)] + '...' * (K < L))
