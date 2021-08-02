N = int(input())
D = list(map(int, input().split()))
print(sum([D[i] * D[j] for i in range(N) for j in range(i + 1, N)]))
