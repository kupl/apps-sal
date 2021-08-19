k = int(input())
que = [i for i in range(1, 10)]
# print(que)
for i in range(k):
    now = que.pop(0)
    too = now % 10

    if too != 0:
        que.append(now * 10 + too - 1)

    que.append(now * 10 + too)

    if too != 9:
        que.append(now * 10 + too + 1)

print(now)
