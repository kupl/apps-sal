import heapq
(N, C) = list(map(int, input().split()))
ans = C
d = [list() for _ in range(C + 1)]
for _ in range(N):
    (s, t, c) = list(map(int, input().split()))
    d[c].append([s, t])
S = [0] * (10 ** 5 + 1)
T = [0] * (10 ** 5 + 1)
for i in range(C + 1):
    if not d[i]:
        continue
    d[i].sort()
    (s, t) = d[i][0]
    for j in range(1, len(d[i])):
        if t == d[i][j][0]:
            t = d[i][j][1]
        else:
            S[s] += 1
            T[t] += 1
            (s, t) = d[i][j]
    S[s] += 1
    T[t] += 1
temp = 0
ans = 0
for i in range(1, 10 ** 5 + 1):
    temp += S[i] - T[i - 1]
    ans = max(ans, temp)
print(ans)
