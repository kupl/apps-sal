(A, B, N) = map(int, input().split())
if N < B:
    print(int(A * N / B) - A * int(N / B))
if B <= N:
    print(int(A * (B - 1) / B) - A * int((B - 1) / B))
