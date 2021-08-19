(N, X) = list(map(int, input().split()))
ms = [int(input()) for i in range(N)]
print(N + (X - sum(ms)) // min(ms))
