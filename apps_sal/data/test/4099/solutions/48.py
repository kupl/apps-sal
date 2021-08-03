N, K, M = map(int, input().split())
data = list(map(int, input().split()))

sum_data = sum(data)
result = N * M - sum_data

if result > K:
    print("-1")

elif result <= 0:
    print("0")

else:
    print(result)
