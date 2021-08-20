n = int(input())
P = list(map(int, input().split()))
cnt = 0
for i in range(1, n - 1):
    if min(P[i - 1], P[i], P[i + 1]) < P[i] and max(P[i - 1], P[i], P[i + 1]) > P[i]:
        cnt += 1
print(cnt)
