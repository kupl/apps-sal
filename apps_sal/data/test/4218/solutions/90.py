N = int(input())
L = [i for i in range(1, N + 1) if i % 2 != 0]
A = len(L) / N
print(A)
