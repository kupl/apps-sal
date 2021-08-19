(n, m, k) = map(int, input().split())
chatsmembers = []
chatkol = []
for i in range(n):
    chatsmembers.append(list(map(int, input().split())))
chatkol = [0] * m
chatsents = [0] * n
for i in range(k):
    (a, b) = map(int, input().split())
    chatsents[a - 1] += 1
    chatkol[b - 1] += 1
for i in range(n):
    t = 0
    for j in range(m):
        if chatsmembers[i][j] == 1:
            t += chatkol[j]
    print(t - chatsents[i], end=' ')
