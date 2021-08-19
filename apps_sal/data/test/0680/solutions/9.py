friends = []
for i in range(3):
    X, Y = map(int, input().split())
    friends.append((X, Y))

result = []

friends = sorted(friends)

for i in range(friends[0][0], friends[1][0]):  # X increment
    result.append((i, friends[0][1]))
for i in range(friends[1][0] + 1, friends[2][0] + 1):
    result.append((i, friends[2][1]))

mean_x = friends[1][0]
friends = sorted(friends, key=lambda x: x[1])
for i in range(friends[0][1], friends[2][1] + 1):  # Y increment
    result.append((mean_x, i))

print(len(result))
for item in result:
    print(item[0], item[1])
