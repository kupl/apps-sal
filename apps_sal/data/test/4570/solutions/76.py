N, A, B = list(map(int, input().split()))

park_price = []
park_price.append(N * A)
park_price.append(B)

answer = min(park_price)
print(answer)
