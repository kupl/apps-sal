N = int(input())
P = [(0, 0, 0)]
for i in range(N):
    (t, x, y) = map(int, input().split())
    P.append((t, x, y))
T = [0] * N
dist = [0] * N
for i in range(N):
    T[i] = P[i + 1][0] - P[i][0]
    dist[i] = abs(P[i + 1][1] - P[i][1]) + abs(P[i + 1][2] - P[i][2])
ans = 1
for i in range(N):
    if dist[i] > T[i]:
        ans = 0
    else:
        m = T[i] - dist[i]
        if m % 2 == 0:
            pass
        else:
            ans = 0
    if ans == 0:
        break
print('Yes' if ans == 1 else 'No')
