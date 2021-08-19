def R():
    return map(int, input().split())


(n, m, k) = R()
chat = []
for i in range(n):
    chat.append(list(R()))
man = [0] * n
room = [0] * m
for i in range(k):
    (a, b) = R()
    man[a - 1] += 1
    room[b - 1] += 1
for i in range(n):
    t = 0
    for j in range(m):
        if chat[i][j] == 1:
            t += room[j]
    print(t - man[i], end=' ')
