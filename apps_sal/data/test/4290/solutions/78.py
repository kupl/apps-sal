[N, M] = [int(i) for i in input().split()]
print(int(N*max(N-1, 0)/2) + int(M*max(M-1, 0)/2))
