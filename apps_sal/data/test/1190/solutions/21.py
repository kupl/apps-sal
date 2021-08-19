(w1, h1, w2, h2) = list(map(int, input().split()))
answer = 4 + (h1 + h2) * 2 + w1 + w2 + abs(w2 - w1)
print(answer)
