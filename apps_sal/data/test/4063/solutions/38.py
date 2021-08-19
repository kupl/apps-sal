# ABC132 C

N = int(input())
D = list(map(int, input().split()))
D.sort()
A = list(range(D[int(N / 2) - 1] + 1, D[int(N / 2)] + 1))

print(len(A))
