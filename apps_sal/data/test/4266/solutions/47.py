K, X = map(int,input().split())

possble_black = []

for i in range(X - K + 1,X+K):
    possble_black.append(i)
# X = X-K+1
# for j in range(K - 1):
#     stone2 = X
#     possble_black.append(stone2)
#     X -= 1
possble_black = [str(a) for a in possble_black]
possble_black = " ".join(possble_black)
print(possble_black)
