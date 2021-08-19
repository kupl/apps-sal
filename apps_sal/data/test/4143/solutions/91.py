N = int(input())
A = [int(input()) for _ in range(5)]
print((N - 1) // min(A) + 1 + 4)
