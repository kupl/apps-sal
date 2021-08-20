(N, X) = map(int, input().split())
mi = [int(input()) for _ in range(N)]
print(N + (X - sum(mi)) // min(mi))
