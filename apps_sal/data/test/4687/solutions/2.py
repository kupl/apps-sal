N, K = map(int, input().split())
s = 0
ab = [[0, 0] for i in range(N)]
for i in range(N):
    ab[i][0], ab[i][1] = map(int, input().split())
ab = sorted(ab)

# print(ab)
for i in range(N):
    s += ab[i][1]
    if s >= K:
        print(ab[i][0])
        break
