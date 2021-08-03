N, K = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(N)]

ls.sort(key=lambda x: x[0])
s = 0

for i in range(N):
    s += ls[i][1]
    if s >= K:
        break

print(ls[i][0])
