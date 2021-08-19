(N, A, B, C, D, E) = [int(input()) for _ in range(6)]
ans = -(-N // min(A, B, C, D, E)) + 4
print(ans)
