N, M = map(int, input().split())

data = list(map(int, input().split()))

if N - sum(data) >= 0:
    print(N-sum(data))
else:
    print(-1)
