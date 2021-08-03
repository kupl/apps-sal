N, M = map(int, input().split())
mini = 0
maxi = N
for _ in range(M):
    mini1, maxi1 = map(int, input().split())
    mini = max(mini, mini1)
    maxi = min(maxi, maxi1)
print(max(maxi - mini + 1, 0))
