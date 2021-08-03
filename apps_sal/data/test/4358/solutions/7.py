N = int(input())
P = sorted([int(input()) for x in range(N)])

m = P[N - 1]
P = P[:N - 1]
print(sum(P) + m // 2)
