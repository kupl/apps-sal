N, M = map(int, input().split())
max_L = 1
min_R = N
for _ in range(M):
    L, R = map(int, input().split())
    max_L = max(L, max_L)
    min_R = min(R, min_R)

if min_R - max_L < 0:
    print(0)
else:
    print(min_R - max_L + 1)
