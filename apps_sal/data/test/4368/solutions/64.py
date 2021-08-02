N, K = map(int, input().split())

D = []
while (N > 0):
    D.append(N % K)
    N = N // K

print(len(D))
