(N, K, C) = map(int, input().split())
S = input()
day = []
for i in range(len(S)):
    if S[i] == 'o':
        day.append(i + 1)
E = [day[0]]
cur = day[0]
for i in range(1, len(day)):
    if day[i] >= cur + C + 1:
        cur = day[i]
        E.append(cur)
F = [day[len(day) - 1]]
cur = day[len(day) - 1]
for i in range(len(day) - 1, -1, -1):
    if day[i] <= cur - C - 1:
        cur = day[i]
        F.append(cur)
if len(E) > K:
    while len(E) > K:
        E.pop()
if len(F) > K:
    while len(F) > K:
        F.pop()
F.reverse()
for i in range(K):
    if E[i] == F[i]:
        print(E[i])
