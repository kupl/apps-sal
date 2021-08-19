(N, M) = map(int, input().split())
food = []
for i in range(N):
    food.append(list(map(int, input().split())))
like = [0 for i in range(M)]
for i in range(N):
    for j in range(food[i][0]):
        like[food[i][j + 1] - 1] += 1
print(like.count(N))
