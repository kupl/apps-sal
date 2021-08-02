N, K = map(int, input().split())

result = N % K
if result <= abs(result - K):
    print(result)
elif result > abs(result - K):
    result = abs(result - K)
    print(result)
