n = int(input())
A = [int(x) for x in input().split()]
s = sum(A)
M = max(A)
for K in range(M, M + 300):
    votes = K * n - s
    if votes > s:
        print(K)
        break
