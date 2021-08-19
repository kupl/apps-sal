N = int(input())
P = list(map(int, input().split()))
T = [P[0]] + [10 ** 10] * (N - 1)
ans = 0
for i in range(N):
    T[i] = min(T[i - 1], P[i])
for i in range(N):
    if P[i] <= T[i]:
        ans += 1
print(ans)
