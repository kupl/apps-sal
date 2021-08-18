K, X = map(int, input().split())

possble_black = []

for i in range(X - K + 1, X + K):
    possble_black.append(i)
possble_black = [str(a) for a in possble_black]
possble_black = " ".join(possble_black)
print(possble_black)
