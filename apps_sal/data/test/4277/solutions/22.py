(n, a, b) = list(map(int, input().split()))
train = n * a
taxi = b
answer = min(train, taxi)
print(answer)
