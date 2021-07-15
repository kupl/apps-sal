N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

res = N - sum(A)
print(res if res >= 0 else -1)
