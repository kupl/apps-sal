N = int(input())
P = list(map(int, input().split()))
cnt = 0
for (i, j) in enumerate(P):
    if i + 1 == j and i == N - 1:
        (P[i - 1], P[i]) = (P[i], P[i - 1])
        cnt += 1
        continue
    if i + 1 == j:
        (P[i + 1], P[i]) = (P[i], P[i + 1])
        cnt += 1
print(cnt)
