A, B, C, K = map(int, input().split())

num_A = min(A, K)
num_B = min(B, K - num_A)
num_C = min(C, K - num_A - num_B)

print(num_A - num_C)
