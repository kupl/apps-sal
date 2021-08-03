N, M = map(int, input().split())
day = list(map(int, input().split()))
total = 0
for i in range(M):
    total += day[i]
if N >= total:
    print(N - total)
else:
    print('-1')
