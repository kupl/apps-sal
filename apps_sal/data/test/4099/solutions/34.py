N, K, M = map(int, input().split())
scores = list(map(int, input().split()))

x = M * N - sum(scores)

if x > K:
    print("-1")
if 0 < x <= K:
    print(x)
if x <= 0:
    print(0)
