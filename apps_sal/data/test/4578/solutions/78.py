N, X = [int(i) for i in input().split()]
M = [int(input()) for _ in range(N)]
print((N + ((X - (sum(M))) // min(M))))

